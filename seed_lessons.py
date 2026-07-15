from app import app, db, Lesson

lessons = [
    {
        "category": "Phishing",
        "title": "Phishing & Social Engineering",
        "icon": "🎣",
        "summary": "How attackers trick you into handing over your credentials or trust.",
        "content": """Phishing is when attackers impersonate a trusted source (your university, bank, or a company) to trick you into clicking a link, entering your password, or sharing personal information.

COMMON SIGNS:
- Urgent language ("Act now or your account will be suspended")
- Links that look almost right but aren't (e.g., portal-nwus.free.site instead of your real school domain)
- Generic greetings like "Dear Student" instead of your actual name
- Requests to "verify" your password or login details

REAL EXAMPLE:
An email arrives claiming your course registration is incomplete, with a link to "log in immediately" to avoid exam clearance cancellation. The link leads to a fake page designed to steal your portal login.

HOW TO PROTECT YOURSELF:
1. Never click links in unexpected emails/messages asking you to log in
2. Go directly to the official website/app yourself instead
3. Check the actual URL carefully before entering any information
4. When in doubt, contact the organization directly through official channels"""
    },
    {
        "category": "Password & MFA",
        "title": "Password & Account Security",
        "icon": "🔐",
        "summary": "Strong passwords and multi-factor authentication are your first line of defense.",
        "content": """Your password is the main gate protecting your accounts. Weak or reused passwords are one of the most common ways accounts get compromised.

KEY RULES:
- Use a different password for every important account
- Longer passphrases are stronger than short complex ones (e.g., "PurpleTiger$RunsFast42" beats "P@ss1")
- Enable Multi-Factor Authentication (MFA/2FA) wherever available — it protects you even if your password leaks

THE OTP TRICK (VERY COMMON IN NIGERIA):
Someone messages you on WhatsApp claiming they "accidentally" sent their verification code to your number and asks you to forward it. That code is actually for YOUR account — sending it lets them take over your WhatsApp.

RULE TO REMEMBER: Never share an OTP or verification code with anyone, no matter who they claim to be — not your bank, not "IT support," not a stranger claiming it's a mistake.

HOW TO PROTECT YOURSELF:
1. Use a password manager if possible to avoid reusing passwords
2. Turn on MFA on your email, social media, and banking apps
3. Never share OTPs/verification codes with anyone"""
    },
    {
        "category": "Mobile Security",
        "title": "Mobile & Device Security",
        "icon": "📱",
        "summary": "Your phone holds your whole digital life — protect it like it matters, because it does.",
        "content": """Your phone is often more valuable to an attacker than your laptop — it has your banking apps, messages, photos, and social accounts all in one place.

KEY RISKS:
- Installing apps from outside official app stores (sideloading APKs) — these skip security screening
- Using public Wi-Fi for sensitive activity like banking
- Ignoring software updates, which patch known security holes
- Losing your phone without a lock screen or remote-wipe option set up

REAL EXAMPLE:
A "free cracked version" of a paid app is offered as a direct APK download instead of through the Play Store. Installing it can silently install malware that steals your data or messages.

HOW TO PROTECT YOURSELF:
1. Only install apps from official app stores
2. Avoid sensitive activity (banking, login) on public Wi-Fi — use mobile data or a VPN instead
3. Keep your phone's software updated
4. Set a strong lock screen and enable "Find My Device" features"""
    },
    {
        "category": "Malware & Browsing",
        "title": "Malware & Safe Browsing",
        "icon": "🛡️",
        "summary": "Recognizing malicious downloads, fake warnings, and disguised files.",
        "content": """Malware is malicious software designed to damage, steal from, or spy on your device. It often disguises itself as something helpful or harmless.

COMMON TRICKS:
- Pirated software/textbooks disguised as free downloads
- Pop-ups claiming "Your device is infected! Click here to scan" (this is fake and often installs the very malware it claims to remove)
- Files with double extensions like "Invoice.pdf.exe" or "Result.docx.scr" — these are programs disguised as documents

REAL EXAMPLE:
A browser tab suddenly shows a loud warning: "Virus detected! Call this number immediately." This is a scare tactic — real operating systems don't alert you this way. Closing the tab is the safe response, not calling the number.

HOW TO PROTECT YOURSELF:
1. Avoid downloading pirated/cracked software or documents
2. Never trust urgent pop-up warnings — close them without clicking
3. Check file extensions carefully before opening attachments
4. Keep antivirus/security software updated"""
    },
    {
        "category": "Social Media & Privacy",
        "title": "Social Media & Privacy",
        "icon": "🔒",
        "summary": "What you share online can be used against you — including in serious ways like sextortion.",
        "content": """Oversharing on social media can expose you to stalking, identity theft, and scams — sometimes with serious emotional and financial consequences.

KEY RISKS:
- Publicly sharing your location, routine, or travel plans
- Public profiles that expose your phone number, school, or daily habits
- Fast-moving online relationships that quickly ask for intimate photos

SEXTORTION (A SERIOUS AND GROWING THREAT):
A new online contact builds a close relationship quickly, then asks for intimate photos or videos, and later threatens to share them unless you pay. This is a crime, not a personal failure. If it happens to you: do not pay, stop engaging, save evidence, and report it to the platform and trusted authorities.

HOW TO PROTECT YOURSELF:
1. Review and restrict your privacy settings
2. Be cautious of anyone moving a relationship very fast online
3. Never send intimate content, even to someone you trust
4. If targeted by sextortion, don't pay — report and seek support immediately"""
    },
    {
        "category": "Financial Scams",
        "title": "Financial & Fintech Scams",
        "icon": "💰",
        "summary": "Fake alerts, task scams, and giveaway tricks designed to drain your account.",
        "content": """Financial scams are designed to trick you into sending money or "verifying" transactions that never actually happened.

COMMON PATTERNS:
- Fake credit alert SMS followed by a call asking you to "refund" a mistaken transfer (no real money was ever sent)
- "Side hustle" job offers that require you to pay a registration fee or buy crypto to "unlock" paid tasks
- Unsolicited "you've won a giveaway" messages asking you to click a link or share your details to claim a prize

GOLDEN RULE: Legitimate employers and giveaways never require you to pay money to receive money.

REAL EXAMPLE:
A Telegram channel offers $50/day for "social media review tasks" but asks for a ₦3,000 registration fee first. This is a scam designed to collect fees from as many people as possible — there's no real job.

HOW TO PROTECT YOURSELF:
1. Always verify transactions directly in your own bank app, never trust screenshots or SMS alone
2. Never pay money to "unlock" a job or earning opportunity
3. Ignore unsolicited "you've won" messages"""
    },
    {
        "category": "Data Privacy",
        "title": "Data Privacy & Identity Protection",
        "icon": "🪪",
        "summary": "Protecting your NIN, BVN, and personal information from identity theft.",
        "content": """Your personal identification details (NIN, BVN, date of birth, etc.) are valuable to attackers because they can be used to impersonate you or access your financial accounts.

RED FLAGS:
- Forms asking for your NIN/BVN AND your account password together — legitimate processes never need both
- Callers claiming to be from your bank or NIMC asking you to "confirm" your BVN or NIN over the phone
- "Scholarship" or "grant" applications that request sensitive ID numbers alongside login credentials

REAL EXAMPLE:
A "government scholarship" form asks for your full name, NIN, BVN, bank account number, AND your student portal password. No legitimate scholarship needs your password — this combination is designed for identity theft.

HOW TO PROTECT YOURSELF:
1. Never share your NIN/BVN with unsolicited callers or forms
2. Verify any request by contacting the organization directly through official channels
3. Be especially cautious of forms combining ID numbers with passwords"""
    },
    {
        "category": "Incident Response",
        "title": "What To Do If You're Compromised",
        "icon": "🚨",
        "summary": "Quick, calm action after a security incident limits the damage significantly.",
        "content": """Even careful people can be targeted. What matters most is how quickly and calmly you respond.

IF YOU ENTERED YOUR PASSWORD ON A FAKE SITE:
1. Change that password immediately
2. Change it everywhere else you reused it
3. Enable MFA if you haven't already

IF YOU SUSPECT AN ACCOUNT WAS ACCESSED:
1. Change the password right away
2. Check and revoke any active sessions or connected devices you don't recognize
3. Review recent activity for anything unfamiliar

IF YOU ENCOUNTER A SCAM (even if you didn't fall for it):
Report or block the sender, and report impersonation to the real organization being impersonated. This helps protect others too.

REMEMBER: Acting fast limits damage. Panic and silence make things worse — reporting and quick action are always the right response, not embarrassment or hiding what happened."""
    },
]

def seed():
    with app.app_context():
        if Lesson.query.first():
            print("Lessons already exist. Skipping seeding.")
            return
        for l in lessons:
            db.session.add(Lesson(**l))
        db.session.commit()
        print(f"Seeded {len(lessons)} lessons successfully.")

if __name__ == '__main__':
    seed()