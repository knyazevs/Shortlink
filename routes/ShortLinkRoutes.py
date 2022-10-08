from flask import render_template, redirect, Blueprint

from forms.LinkForm import LinkForm
from services.ShortLinkGenerator import get_shortlink, get_long_link

shortlink_page = Blueprint('shortlink_page', __name__, template_folder='templates')


@shortlink_page.route('/', methods=["GET", "POST"])
def main():
    link_input = LinkForm()
    if link_input.validate_on_submit():
        short_link = get_shortlink(link_input.url.data,
                                   link_input.name.data,
                                   link_input.author.data,
                                   link_input.deadline.data)
        return render_template('result.html', short_link=short_link)
    return render_template('index.html', form=link_input)


@shortlink_page.route('/<short_link>')
def short_link_redirect(short_link):
    try:
        long_link = get_long_link(short_link)
        return redirect(long_link)
    except:
        return render_template('404.html')
