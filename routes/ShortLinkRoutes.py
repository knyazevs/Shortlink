from flask import render_template, session, redirect, Blueprint

from forms.LinkForm import LinkForm
from services.ShortLinkGenerator import get_shortlink, get_long_link

shortlink_page = Blueprint('shortlink_page', __name__, template_folder='templates')


@shortlink_page.route('/', methods=["GET", "POST"])
def main():
    link_input = LinkForm()
    if link_input.validate_on_submit():
        url = link_input.url.data
        session['long_link'] = url
        long_link = session.get('long_link')
        session['short_link'] = get_shortlink(long_link)
        print(session['short_link'])
        return render_template('result.html', short_link=session.get('short_link'))
    return render_template('index.html', form=link_input)


@shortlink_page.route('/<short_link>')
def short_link_redirect(short_link):
    try:
        long_link = get_long_link(short_link)
        return redirect(long_link)
    except:
        return render_template('404.html')
