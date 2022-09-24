# pip install mailjet_rest
from mailjet_rest import Client

# for internet connection test
from requests import get, ConnectionError, Timeout

# for email validation
from re import compile, fullmatch


class EmailHelper:

    def is_email_valid(self, email_to: str) -> bool:
        """
        This method used to check validation of given email which is in that format
        (username)@(domain_name).(top-level_domain) :param email_to:<str> email to check validation
        :return:<bool> Valid or Invalid
        """
        regex = compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
        if fullmatch(regex, email_to):
            return True
        else:
            return False

    def check_internet_connection(self) -> bool:
        """
        This method used to check internet connection.
        :return: <bool> Internet connected or disconnected
        """
        try:
            get("https://www.google.com.tr/")
            return True
        except (ConnectionError, Timeout):
            return False


class Email(EmailHelper):

    def __init__(self, api_key: str, api_secret: str) -> None:
        """
        Initialize mailjet object with api_key and api_secret for further mail send usage
        :param api_key: <str> api_key used for mailjet Client
        :param api_secret: <str> api_secret used for mailjet Client
        """
        self.mailjet_obj = Client(auth=(api_key, api_secret), version="v3.1")

    def send_email(
        self,
        mail_from: str,
        sender_name: str,
        mail_to: str,
        receiver_name: str = "God knows",
        mail_subject: str = "Unkown",
    ) -> bool:
        """
        This method used to send email to only one receiver.
        You can manipulate mail content and send to receiver address
        :param mail_from: <str> sender mail address
        :param sender_name:  <str> sender name if it's known
        :param mail_to: <str> receiver mail address
        :param receiver_name:  <str> receiver name if it's known
        :param mail_subject: <str> mail subject if it's existed
        :return: <bool> Mail successfully sent or not
        """
        # inherited from EmailHelper class to check internet connection and mail validation
        if (not self.is_email_valid(mail_to) and
                not self.check_internet_connection() and
                not self.is_email_valid(mail_from)):
            return False
        else:
            # read template mail from html file
            with open("template_mail.html", "r") as mail_template:
                data = mail_template.read()
            # initialize mail object
            mail_details = {
                "Messages": [{
                    "From": {
                        "Email": f"{mail_from}",
                        "Name": f"{sender_name}"
                    },
                    "To": [{
                        "Email": f"{mail_to}",
                        "Name": f"{receiver_name}"
                    }],
                    "Subject": f"{mail_subject}",
                    "TextPart": "My first Mailjet email",
                    "HTMLPart": f"{data}",
                    "CustomID": "AppGettingStartedTest",
                }]
            }
            # send mail to receiver
            result = self.mailjet_obj.send.create(data=mail_details)
            if result.status_code == 200:
                return True
            else:
                return False


if __name__ == "__main__":
    email_obj = Email(api_key="your_api_key", api_secret="your_api_secret")
    email_obj.send_email(
        mail_from="sender_mail",
        sender_name="sender_name",
        mail_to="receiver_email",
        receiver_name="receiver_name",
        mail_subject="Hello Fucking World !",
    )
