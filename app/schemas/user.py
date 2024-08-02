from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class MembershipCode(BaseModel):
    code: str
    value: int
    is_percentage: bool
    expiration_date: datetime
    assignment_date: datetime


class PromoCode(BaseModel):
    code: str
    value: int
    applied: bool
    assignment_date: datetime
    expiration_date: datetime
    previous_values: List[str]  # Suponiendo que los valores anteriores sean cadenas


class Coordinates(BaseModel):
    lat: float
    lon: float


class User(BaseModel):
    _id: str
    membership_code: MembershipCode
    promo_code: PromoCode
    coordinates: Coordinates
    isClient: bool
    role: str
    photos: List[str]  # Lista de URLs de fotos
    emails: List[str]  # Lista de correos electrónicos
    images: List[str]  # Lista de URLs de imágenes
    fbFriendsIds: List[str]  # Lista de IDs de amigos en Facebook
    friends: List[str]
    artistsRecentlyPlayed: List[str]
    artistsFollowed: List[str]
    music: List[str]
    music_category: List[str]
    sports: List[str]
    sports_category: List[str]
    theatre: List[str]
    special_events: List[str]
    birthdayToogle: bool
    likesToogle: bool
    emailToogle: bool
    notificationToogle: bool
    botNotificationToogle: bool
    tipo: str
    fb_group_code: str
    created: datetime
    email: str
    password: str
    firstName: str
    lastName: str
    imgSrc: str
    __v: int
    mailchimpUserID: str


# def user_entity(user: Dict) -> Dict:
#     return user


# def users_entity(users: List[Dict]) -> List[Dict]:
#     return [user_entity(user) for user in users]
