# Problem number 929
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = []
        for email in emails:
            email_splitted = email.split("@")
            local_name = email_splitted[0]
            domain_name = email_splitted[1]
            # Ignore everything after '+' in local_name
            local_name = local_name.split("+")[0]
            # local_name without '.'s
            local_name = local_name.split(".")
            local_name = ''.join(local_name)
            
            final_email = local_name + '@' + domain_name
            
            if final_email not in unique_emails:
                unique_emails.append(final_email)
                
        return (len(unique_emails))
