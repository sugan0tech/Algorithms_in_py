import re
pss = str(input("Type your password>"))
def check_password(password):
    score_index = 0
    if len(password) > 8:
        score_index += 1
        #calculating no of upper, lower, special characters
        lower_c = 0
        upper_c = 0
        alpha_c = 0
        num_str = "" #string of the number in exact
        for i in password:
            if i.islower():
                lower_c += 1
            elif i.isupper():
                upper_c += 1
            elif re.match("[@_!#$%^&*()<>?/|}{~:]", i):
                alpha_c += 1
            elif i.isdigit():
                num_str += i
        if lower_c >= 3:
            score_index += 1
        if  upper_c >= 1:
            score_index += 1
        if alpha_c >= 1:
            score_index += 1
        if not (re.match("1234567890", num_str)) and (len(num_str) >= 3):
            score_index += 1
    score_str = ["weakest", "weak", "average", "medium", "strong", "strongest"]
    return score_str[score_index]


print(check_password(pss))