from users.models import User


def userinfo(claims: dict, user: User) -> dict:
    claims["name"] = f"{user.first_name} {user.last_name}"
    claims["given_name"] = user.first_name
    claims["family_name"] = user.last_name
    claims["email"] = user.email
    claims["email_verified"] = False
    claims["steam_id"] = "0000"
    return claims
