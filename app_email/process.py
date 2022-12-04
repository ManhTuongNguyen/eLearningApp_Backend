import re
import smtplib
from email.mime.text import MIMEText


class EmailHelper:
    username = ''
    password = ''

    def send_email(self, subject: str, content: str, to_address: str) -> bool:
        crypto = CeasarHelper()
        username = crypto.decrypt(self.username, 6)
        password = crypto.decrypt(self.password, 3)

        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['from'] = username
        msg['To'] = to_address

        # Send message using smtp server
        try:
            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            server.starttls()
            server.ehlo()
            server.login(username, password)
            server.sendmail(username, to_address, msg.as_string())
            server.quit()
            return True
        except Exception as ex:
            print(ex)
            return False


def is_valid_email(email: str) -> bool:
    if not email.strip():
        raise Exception("Không được bỏ trống địa chỉ email!")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        if email.endswith((".com", ".co.uk", ".fr", ".ru", ".vn", ".net")):
            # https://email-verify.my-addr.com/list-of-most-popular-email-domains.php#:~:text=Top%20100%20%20%201%20%20%20gmail.com,%20%201.27%25%20%2095%20more%20rows%20
            return True
        raise Exception("Địa chỉ email không được chấp nhận tại hệ thống!")
    raise Exception("Địa chỉ email không hợp lệ!")


class CeasarHelper:
    bangTra = ['C', 'D', '-', '=', '_', '(', ')', 'E', 'o', 'p', 'z', 'A', '2', 'Z', ';',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '@',
               'Q', 'R', 'S', 'q', 'v', 'w', 'x', 'y', 'T', '6', '7', '9', '.', '3', '*',
               'r', 's', 't', 'u', 'F', 'G', 'H', 'L', 'M', 'N', 'O', 'P', 'V', 'W', '/',
               '4', 'X', 'Y', '0', '1', '5', '!', '+', 'I', 'B', ',', 'U', ' ', 'J', 'K', ]

    def encrypt(self, raw_str: str, key: int = None) -> str:
        """ Encrypt string using Ceasar Algorithm
        Args:
            raw_str: String need encrypt
            key: key using to encrypt string
        Return:
            String encrypted using Ceasar algorithm
        Raise:
            Raise Exception if key is not number
        """
        if key is None:
            key = 5
        if type(key) != int:
            raise Exception('Key must be a number!')
        encrypted = ''
        for i in raw_str:
            old_index = -1
            try:
                old_index = self.bangTra.index(i)
            except:
                old_index = -1
            if old_index == -1:
                encrypted += i
                continue
            new_index = old_index + key
            while new_index < 0:
                new_index += len(self.bangTra)
            while new_index > len(self.bangTra) - 1:
                new_index -= len(self.bangTra)
            encrypted += self.bangTra[new_index]
        return encrypted

    def decrypt(self, raw_str: str, key: int = None) -> str:
        """
        Decrypt string using Ceasar Algorithm
        Args:
            raw_str: String need decrypt
            key: key using to decrypt string
        Return:
            string decrypt using ceasar algorithm
        Raise:
            Raise Exception if key is not number
        """
        if key is None:
            key = 5
        if type(key) != int:
            raise Exception('Key must be a number!')
        decrypted = ''
        for i in raw_str:
            old_index = -1
            try:
                old_index = self.bangTra.index(i)
            except:
                old_index = -1
            if old_index == -1:
                decrypted += i
                continue
            new_index = old_index - key
            while new_index < 0:
                new_index += len(self.bangTra)
            while new_index > len(self.bangTra) - 1:
                new_index -= len(self.bangTra)
            decrypted += self.bangTra[new_index]
        return decrypted
