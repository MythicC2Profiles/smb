from mythic_container.C2ProfileBase import *
from pathlib import Path
import os

class SMB(C2Profile):
    name = "smb"
    description = "Communication over SMB named pipes with a specific packet structure.\nCheck out the docs for more information."
    author = "@djhohnstein, @its_a_feature_"
    is_p2p = True
    is_server_routed = True
    semver = "0.1.0"
    agent_icon_path = Path(".") / "smb" / "c2_functions" / "smb.svg"
    server_binary_path = Path(os.path.join(".", "smb", "c2_code"))
    server_folder_path = Path(os.path.join(".", "smb", "c2_code"))
    parameters = [
        C2ProfileParameter(
            name="pipename",
            description="Named Pipe to create",
            format_string="[a-z0-9]{8}\-[a-z0-9]{4}\-[a-z0-9]{4}\-[a-z0-9]{4}\-[a-z0-9]{12}",
            randomize=True,
            required=False,
        ),
        C2ProfileParameter(
            name="killdate",
            description="Kill Date",
            parameter_type=ParameterType.Date,
            default_value=365,
            required=False,
        ),
        C2ProfileParameter(
            name="encrypted_exchange_check",
            description="Perform Key Exchange",
            default_value=True,
            required=False,
            parameter_type=ParameterType.Boolean,
        ),
        C2ProfileParameter(
            name="AESPSK",
            description="Crypto type",
            default_value="aes256_hmac",
            parameter_type=ParameterType.ChooseOne,
            choices=["aes256_hmac", "none"],
            required=False,
            crypto_type=True
        ),
    ]
