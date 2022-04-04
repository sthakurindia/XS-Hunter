# XS-Hunter
Python CLI tool for finding XSS and SQL injection

# INSTALL
git clone https://github.com/sthakurindia/XS-Hunter.git
cd XS-Hunter
pip install -r requirements.txt

NOTE :- Intsall gf and Patterns
tomnomnom gf tool - https://github.com/tomnomnom/gf

gf patterns - https://github.com/1ndianl33t/Gf-Patterns

# HOW TO USE
[xss]
echo http://testphp.vulnweb.com | gau | gf xss | python3 xshunter.py -m xss

[SQL]
echo http://testphp.vulnweb.com | gau | gf sqli | python3 xshunter.py -m sqli

[output]
-o test.txt

# QSREPLACE XSS
echo http://testphp.vulnweb.com | gau | gf xss | qsreplace '<script>alert(1)</script>' | python3 xshunter.py

# DEMO
![ezgif com-gif-maker](https://user-images.githubusercontent.com/74065510/161495203-149d5fef-754a-456f-bad8-227dc5e381d5.gif)
