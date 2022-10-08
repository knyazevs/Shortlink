from datetime import datetime

from hashids import Hashids

from entities.LinkEntity import LinkEntity
import shortuuid

hashids = Hashids(salt="this is my salt")


def get_shortlink(long_link, name, author, deadline):
    try:
        existing_link = LinkEntity.get(LinkEntity.real_address == long_link,
                                       LinkEntity.name == name,
                                       LinkEntity.author == author,
                                       LinkEntity.deadline == deadline)
        if existing_link:
            return existing_link.local_address
    except:
        pass

    return generate_short_link(long_link, name, author, deadline)


def generate_short_link(long_link, name, author, deadline):
    short_uuid = shortuuid.uuid()
    print(f"{long_link}: {short_uuid}")
    link_entity = LinkEntity.create(real_address=long_link, local_address=short_uuid, name=name, author=author,
                                    deadline=deadline)
    short_id = hashids.encode(link_entity.id)
    link_entity.local_address = short_id
    link_entity.save()
    return short_id


def get_long_link(short_link):
    link_id = hashids.decode(short_link)
    link_entity = LinkEntity.select().where(LinkEntity.id == link_id).get()
    present = datetime.now()
    if link_entity.deadline is not None and present > link_entity.deadline:
        print(link_entity.deadline)
        link_entity.delete_instance()
        raise ValueError('Link not found')

    return link_entity.real_address
