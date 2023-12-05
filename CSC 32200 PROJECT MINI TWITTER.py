class User:
    """
    A base class to represent a generic user in the system.
    """
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.balance = 0
        self.reads = 0
        self.likes = 0
        self.dislikes = 0
        self.complaints = 0
        self.warnings = 0
        self.is_active = True

    def update_balance(self, amount):
        """
        Updates the user's balance, adding or subtracting the specified amount.
        """
        self.balance += amount

    def update_activity(self, reads, likes, dislikes, complaints):
        """
        Updates the user's activity stats.
        """
        self.reads += reads
        self.likes += likes
        self.dislikes += dislikes
        self.complaints += complaints

    def check_warnings(self):
        """
        Checks if warnings exceed a certain threshold.
        """
        return self.warnings >= 3

    def deactivate(self):
        """
        Deactivates the user account.
        """
        self.is_active = False


class CorporateUser(User):
    """
    A subclass to represent a corporate user in the system, inheriting from User.
    """
    def __init__(self, user_id, username, corporate_id):
        super().__init__(user_id, username)
        self.corporate_id = corporate_id
        self.ads_posted = 0

    def post_ad(self):
        """
        Allows the corporate user to post an ad and updates the balance.
        """
        self.ads_posted += 1
        self.update_balance(-0.1)  # Cost for posting an ad

    def apply_for_status(self):
        """
        Allows the corporate user to apply for a super-user status.
        """
        # Placeholder for the application process
        return "Applied for super-user status."

    def pay_fine(self):
        """
        Allows the corporate user to pay a fine to remove complaints.
        """
        if self.complaints > 0:
            fine_amount = self.complaints * 1  # Assuming the fine is $1 per complaint
            if self.balance >= fine_amount:
                self.update_balance(-fine_amount)
                self.complaints = 0
                return "Fine paid successfully."
            else:
                return "Insufficient balance to pay the fine."
        else:
            return "No complaints to pay for."

    def post_message(self, message_length):
        """
        Allows the corporate user to post a message with a certain length.
        """
        if message_length <= 20:
            return "Message posted for free."
        else:
            cost = (message_length - 20) * 0.1
            if self.balance >= cost:
                self.update_balance(-cost)
                return "Message posted with additional cost."
            else:
                return "Insufficient balance to post the message."

    def warn(self):
        """
        Issues a warning to the corporate user.
        """
        self.warnings += 1
        if self.check_warnings():
            self.deactivate()
            return "Account deactivated due to excessive warnings."
        else:
            return "Warning issued."

# Example Usage
corp_user = CorporateUser('123', 'CorpInc', 'C12345')
print(corp_user.apply_for_status())
print(corp_user.post_ad())
print(corp_user.pay_fine())
print(corp_user.post_message(25))
print(corp_user.warn())
print(corp_user.warn())
print(corp_user.warn())  # This should deactivate the account
print(corp_user.is_active)  # Should print False after three warnings
