from django.utils.translation import ugettext as _
from oidc_provider.lib.claims import StandardScopeClaims


class ScopeClaims(StandardScopeClaims):
    info_steam_id = (
        "SteamID",
        _("Access to your SteamID."),
    )

    def scope_steam_id(self):
        return {
            "steam_id": self.userinfo.get("steam_id"),
        }
