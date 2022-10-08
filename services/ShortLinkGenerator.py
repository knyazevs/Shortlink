from entities.LinkEntity import LinkEntity
import shortuuid


def get_shortlink(long_link):
    print("Generate link")
    try:
        existing_link = LinkEntity.get(LinkEntity.real_address == long_link)
        if existing_link:
            return existing_link.local_address
    except:
        pass

    return generate_short_link(long_link)


def generate_short_link(long_link):
    short_link = shortuuid.uuid()
    print(f"{long_link}: {short_link}")
    LinkEntity.create(real_address=long_link, local_address=short_link)
    return short_link


def get_long_link(short_link):
    link_entity = LinkEntity.select().where(LinkEntity.local_address == short_link).get()
    return link_entity.real_address
