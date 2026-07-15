from app import app, db, Scenario

scenarios = [
    # ---------- PHISHING & SOCIAL ENGINEERING (4) ----------
    {
        "category": "Phishing", "icon": "📧",
        "title": "The Urgent Portal Email",
        "story": "You open your email and see: 'URGENT: Your course registration is incomplete. Log in within 24 hours to avoid exam clearance cancellation.' The link is portal-nwus.free.site/login.",
        "option_a": "Click the link immediately and log in to fix it",
        "option_b": "Ignore the email completely and delete it",
        "option_c": "Open your browser separately and go to the official NWUS portal directly to check",
        "option_d": "Reply to the email asking if it's real",
        "outcome_a": "Dangerous. That domain isn't your school's official site. You just entered your real portal password into a fake page — attackers now have your login.",
        "outcome_b": "Partially okay. Ignoring avoids the trap, but if there WAS a real issue, you might miss it. Better to verify through the official channel.",
        "outcome_c": "Best choice! Going directly to the official portal yourself avoids the fake link entirely while still letting you check if there's a real problem.",
        "outcome_d": "Dangerous. Replying confirms your email is active to a scammer and doesn't protect your credentials at all.",
        "points_a": 0, "points_b": 5, "points_c": 10, "points_d": 0
    },
    {
        "category": "Phishing", "icon": "🏦",
        "title": "The Fake IT Support Call",
        "story": "Someone calls claiming to be from your university's IT department. They say your account has 'suspicious activity' and ask you to read out your portal password so they can 'secure' your account.",
        "option_a": "Give them your password since they're IT support",
        "option_b": "Hang up and contact IT directly through the official school number to verify",
        "option_c": "Give them a fake password to see what happens",
        "option_d": "Ask them to email you instead, then give the password by email",
        "outcome_a": "Dangerous. Real IT departments never ask for your password verbally. You just handed your account to an attacker.",
        "outcome_b": "Best choice! Verifying independently through official channels is always the safest move when unsure.",
        "outcome_c": "Risky and unnecessary. Just hang up and verify — there's no need to engage at all.",
        "outcome_d": "Dangerous. Email isn't safer — you'd still be sending your password to an unverified party.",
        "points_a": 0, "points_b": 10, "points_c": 3, "points_d": 0
    },
    {
        "category": "Phishing", "icon": "🎓",
        "title": "The Fake Scholarship Link",
        "story": "A message circulates in your class WhatsApp group: 'FG Undergraduate Scholarship — ₦150,000 for all students! Apply now before slots close: fg-scholarship-ng.net'",
        "option_a": "Click the link and fill out the form quickly before slots run out",
        "option_b": "Search independently for official government scholarship announcements to verify",
        "option_c": "Share it with more people so they don't miss out",
        "option_d": "Click the link but only fill in your name, nothing else",
        "outcome_a": "Dangerous. Urgency plus an unofficial domain are classic scam signs. You may hand over sensitive personal data.",
        "outcome_b": "Best choice! Verifying through official sources (like NELFUND or Ministry of Education) confirms if a scholarship is real.",
        "outcome_c": "Risky. Sharing an unverified link spreads potential harm to others.",
        "outcome_d": "Still risky. Even partial info on a fake form can be a phishing test or lead to further requests.",
        "points_a": 0, "points_b": 10, "points_c": 0, "points_d": 3
    },
    {
        "category": "Phishing", "icon": "💼",
        "title": "The Fake Job Verification",
        "story": "You applied to a real internship online. Days later, you get an email asking you to 'verify your application' by logging into a link with your email and password.",
        "option_a": "Log in through the link since you did apply somewhere",
        "option_b": "Contact the company directly through their official website/email to confirm this request is real",
        "option_c": "Ignore it completely without checking",
        "option_d": "Forward your login details by replying to the email instead of using the link",
        "outcome_a": "Dangerous. Companies don't 'verify applications' by asking for your email password — this steals your login regardless of the real application.",
        "outcome_b": "Best choice! Confirming independently avoids the trap while ensuring you don't miss a real opportunity.",
        "outcome_c": "Partially okay, but you might miss a legitimate follow-up. Verifying is safer than assuming.",
        "outcome_d": "Dangerous. This still hands over your password, just through a different channel.",
        "points_a": 0, "points_b": 10, "points_c": 4, "points_d": 0
    },

    # ---------- NIGERIAN SCAMS (5) ----------
    {
        "category": "Nigerian Scams", "icon": "💳",
        "title": "The Fake Credit Alert",
        "story": "You're selling a phone online. The buyer sends you an SMS: 'Credit Alert: ₦85,000 received.' Then they call, saying they mistakenly sent too much and ask you to refund ₦20,000 to another account before you release the phone.",
        "option_a": "Refund the ₦20,000 immediately since they showed proof",
        "option_b": "Check your actual bank app/balance first before doing anything",
        "option_c": "Release the phone first, then check your balance",
        "option_d": "Ask them to send the correct amount instead of refunding",
        "outcome_a": "Dangerous. The 'alert' was fake — no money was ever sent. You just sent real money to a scammer.",
        "outcome_b": "Best choice! Verifying your actual account balance directly is the only reliable way to confirm a transfer happened.",
        "outcome_c": "Very dangerous. You'd lose both the phone and the money you were tricked into sending.",
        "outcome_d": "Risky but slightly better than paying — still best to verify your balance directly first.",
        "points_a": 0, "points_b": 10, "points_c": 0, "points_d": 3
    },
    {
        "category": "Nigerian Scams", "icon": "🎁",
        "title": "The Surprise Giveaway",
        "story": "You get a text from an unknown number: 'Congratulations! You've been selected for a ₦50,000 network giveaway. Click here to claim: paga-promo-ng.info'",
        "option_a": "Click the link to claim your prize",
        "option_b": "Delete/ignore it — you never entered any giveaway",
        "option_c": "Reply asking for more proof first",
        "option_d": "Click the link but don't enter any personal details",
        "outcome_a": "Dangerous. Unsolicited 'you won' messages are one of the oldest scam formats.",
        "outcome_b": "Best choice! If you never entered anything, there's no legitimate prize to claim — ignoring avoids all risk.",
        "outcome_c": "Unnecessary — engaging at all can confirm your number is active to scammers.",
        "outcome_d": "Still risky. Just visiting such sites can expose your device to malicious scripts/malware.",
        "points_a": 0, "points_b": 10, "points_c": 2, "points_d": 3
    },
    {
        "category": "Nigerian Scams", "icon": "📲",
        "title": "The 'Easy' Task Job",
        "story": "A Telegram channel offers $50/day for 'rating products online.' To start, you're asked to pay a ₦3,000 registration fee or deposit crypto to 'unlock' paid tasks.",
        "option_a": "Pay the ₦3,000 since the daily pay sounds worth it",
        "option_b": "Refuse — legitimate jobs never require payment to start earning",
        "option_c": "Ask others in the group if it's legit first",
        "option_d": "Pay a smaller test amount to see if it's real",
        "outcome_a": "Dangerous. This is a classic task-scam — you'll likely be asked for more 'deposits' before ever seeing real pay.",
        "outcome_b": "Best choice! No real job requires you to pay to start earning — this rule alone protects you from this entire scam category.",
        "outcome_c": "Risky — other members in the group are often scammers/bots posing as satisfied 'earners.'",
        "outcome_d": "Still dangerous — any payment at all confirms you're a willing target for further demands.",
        "points_a": 0, "points_b": 10, "points_c": 2, "points_d": 0
    },
    {
        "category": "Nigerian Scams", "icon": "💕",
        "title": "The Fast-Moving Online Romance",
        "story": "You match with someone online who's very attractive and charming. Within days, they're calling you 'babe' and asking you to move to WhatsApp. Soon after, they ask for intimate photos 'to prove trust.'",
        "option_a": "Send the photos since you feel a real connection",
        "option_b": "Be cautious — this fast-moving pattern is a common precursor to sextortion; avoid sharing intimate content",
        "option_c": "Send just one photo as a compromise",
        "option_d": "Ask them to send theirs first",
        "outcome_a": "Very dangerous. This is a well-documented sextortion setup — photos shared can be used for blackmail.",
        "outcome_b": "Best choice! Recognizing the pattern (fast intimacy + pressure for private content) protects you before any harm occurs.",
        "outcome_c": "Still dangerous. Even one photo can be used for blackmail once shared.",
        "outcome_d": "Doesn't protect you — reciprocity doesn't remove the risk of the images being misused later.",
        "points_a": 0, "points_b": 10, "points_c": 0, "points_d": 2
    },
    {
        "category": "Nigerian Scams", "icon": "🆔",
        "title": "The Grant Application Form",
        "story": "A Facebook post claims: 'Federal Government Youth Grant — ₦150,000 for undergraduates! Apply now.' The form asks for your full name, NIN, BVN, bank account, AND your student portal password.",
        "option_a": "Fill in everything since it's a government grant",
        "option_b": "Recognize the red flag — no legitimate form needs your password alongside your NIN/BVN, and avoid it",
        "option_c": "Fill in your NIN and BVN but skip the password field",
        "option_d": "Search for official confirmation of this grant before doing anything",
        "outcome_a": "Very dangerous. This combination of data enables identity theft and account takeover.",
        "outcome_b": "Best choice! Spotting the impossible combination (password + BVN) is the clearest signal of a scam.",
        "outcome_c": "Still risky — NIN and BVN alone are valuable enough for identity theft.",
        "outcome_d": "Good instinct! Verifying is smart, though recognizing the red flag directly (option B) is the fastest protection.",
        "points_a": 0, "points_b": 10, "points_c": 2, "points_d": 8
    },

    # ---------- MOBILE & WHATSAPP SECURITY (3) ----------
    {
        "category": "Mobile & WhatsApp", "icon": "🔢",
        "title": "The OTP Forward Request",
        "story": "A message from an unknown number on WhatsApp says: 'Hi, I'm adding you to our class group but I accidentally sent my verification code to your number. Can you forward it to me?'",
        "option_a": "Forward the code since they seem to know you",
        "option_b": "Refuse — that code is for YOUR WhatsApp account, not theirs",
        "option_c": "Ask them to prove who they are first, then forward it",
        "option_d": "Forward only part of the code",
        "outcome_a": "Very dangerous. That code lets them take over YOUR WhatsApp account, not theirs.",
        "outcome_b": "Best choice! This is one of the most common WhatsApp account takeover tricks — never forward verification codes to anyone.",
        "outcome_c": "Still risky. No legitimate reason exists for anyone to need your account's verification code, regardless of who they claim to be.",
        "outcome_d": "Dangerous. Even a partial code can sometimes assist an attacker or confirm your account is a target.",
        "points_a": 0, "points_b": 10, "points_c": 2, "points_d": 0
    },
    {
        "category": "Mobile & WhatsApp", "icon": "📥",
        "title": "The Cracked App Download",
        "story": "A friend shares a link to a 'free premium version' of a paid app, downloadable directly as an APK file instead of from the Play Store.",
        "option_a": "Download and install it since it's free",
        "option_b": "Avoid it — sideloaded APKs skip security screening and are a common malware source",
        "option_c": "Download it but scan it with antivirus after installing",
        "option_d": "Ask the friend if it's safe first, then install",
        "outcome_a": "Dangerous. This could silently install malware that steals your data or messages.",
        "outcome_b": "Best choice! Sticking to official app stores avoids this entire risk category.",
        "outcome_c": "Risky — scanning AFTER installing means malware may have already run.",
        "outcome_d": "Not reliable — your friend likely doesn't know if it's actually safe either.",
        "points_a": 0, "points_b": 10, "points_c": 3, "points_d": 2
    },
    {
        "category": "Mobile & WhatsApp", "icon": "📶",
        "title": "The Public Wi-Fi Banking Check",
        "story": "You're at a busy cafe and need to quickly check your bank balance. The cafe offers free public Wi-Fi with no password.",
        "option_a": "Connect to the Wi-Fi and check your bank app quickly",
        "option_b": "Use your mobile data instead for anything sensitive",
        "option_c": "Connect to Wi-Fi but close the app quickly after",
        "option_d": "Ask the cafe staff if the Wi-Fi is 'safe' first",
        "outcome_a": "Risky. Open public Wi-Fi can be intercepted, exposing your banking session to attackers on the same network.",
        "outcome_b": "Best choice! Mobile data is far less exposed to this kind of interception for sensitive activity.",
        "outcome_c": "Still risky — even a quick session can be exposed the moment you connect.",
        "outcome_d": "Not reliable — staff usually can't confirm real technical security of the network.",
        "points_a": 2, "points_b": 10, "points_c": 3, "points_d": 2
    },

    # ---------- PASSWORDS & ACCOUNT TAKEOVER (2) ----------
    {
        "category": "Passwords & Account Takeover", "icon": "🔑",
        "title": "The Reused Password Breach",
        "story": "You get a notification that a website you used years ago was hacked and passwords leaked. You realize you use that same password for your email too.",
        "option_a": "Do nothing since the leak wasn't from your email provider",
        "option_b": "Immediately change your email password and any other account sharing it",
        "option_c": "Wait to see if anything suspicious happens first",
        "option_d": "Change just the leaked site's password, keep the email one the same",
        "outcome_a": "Dangerous. Attackers test leaked passwords across other sites — your email is now at risk.",
        "outcome_b": "Best choice! Acting immediately on all accounts sharing that password closes the vulnerability before it's exploited.",
        "outcome_c": "Risky. By the time something 'happens,' the damage may already be done.",
        "outcome_d": "Still dangerous. The exact risk is your email using the same leaked password.",
        "points_a": 0, "points_b": 10, "points_c": 0, "points_d": 2
    },
    {
        "category": "Passwords & Account Takeover", "icon": "🛡️",
        "title": "The MFA Decision",
        "story": "You're setting up a new email account. It offers to enable Multi-Factor Authentication (MFA), but it looks like an extra step you don't feel like doing right now.",
        "option_a": "Skip it — a strong password is probably enough",
        "option_b": "Enable it now, since it protects you even if your password ever leaks",
        "option_c": "Enable it later once you 'have time'",
        "option_d": "Enable it only for banking apps, skip it for email",
        "outcome_a": "Risky. Even strong passwords can leak through data breaches or phishing — MFA is a critical second layer.",
        "outcome_b": "Best choice! Setting it up immediately means you're protected from day one, not just eventually.",
        "outcome_c": "Risky — 'later' often becomes 'never,' leaving you exposed in the meantime.",
        "outcome_d": "Partial protection. Email is often the recovery point for many other accounts, making it just as critical to protect.",
        "points_a": 2, "points_b": 10, "points_c": 3, "points_d": 5
    },

    # ---------- SOCIAL MEDIA PRIVACY (2) ----------
    {
        "category": "Social Media Privacy", "icon": "✈️",
        "title": "The Travel Announcement",
        "story": "You're excited about a trip and post on Instagram: 'Heading to Lagos for a week! ✈️' along with your flight details and hotel tag, visible publicly.",
        "option_a": "Keep the post as is — friends should know you're excited",
        "option_b": "Post it privately (close friends only) or wait until after the trip to share details",
        "option_c": "Remove the flight details but keep the public post",
        "option_d": "Only post while you're already at the destination",
        "outcome_a": "Risky. Publicly announcing an empty home and your exact travel window can invite theft or stalking.",
        "outcome_b": "Best choice! Restricting visibility or posting after the fact removes the real-time risk entirely.",
        "outcome_c": "Better, but the trip dates alone still hint your home may be unoccupied.",
        "outcome_d": "Good improvement! Posting after arrival avoids revealing your home is currently empty during the trip.",
        "points_a": 0, "points_b": 10, "points_c": 5, "points_d": 8
    },
    {
        "category": "Social Media Privacy", "icon": "📍",
        "title": "The Public Profile Check",
        "story": "You realize your Instagram profile is fully public — showing your school, phone number in your bio, and daily routine through frequent location tags.",
        "option_a": "Leave it, more followers see your content this way",
        "option_b": "Review and restrict your privacy settings, remove sensitive info from your bio",
        "option_c": "Only remove the phone number, keep everything else public",
        "option_d": "Make it private but keep posting location tags",
        "outcome_a": "Risky. This makes it easy for scammers or stalkers to build a detailed profile on you.",
        "outcome_b": "Best choice! Restricting visibility and removing sensitive details closes off multiple risks at once.",
        "outcome_c": "Partial improvement, but school and routine info remain exposed.",
        "outcome_d": "Good improvement, though frequent location tags can still reveal patterns to people who do see them.",
        "points_a": 0, "points_b": 10, "points_c": 4, "points_d": 7
    },

    # ---------- SAFE BROWSING & MALWARE (2) ----------
    {
        "category": "Safe Browsing & Malware", "icon": "⚠️",
        "title": "The Scary Pop-up",
        "story": "While browsing, a loud pop-up suddenly appears: 'WARNING! Your device is infected with 5 viruses! Click here to scan now.'",
        "option_a": "Click 'scan now' to fix the infection immediately",
        "option_b": "Close the tab/pop-up without clicking anything",
        "option_c": "Call the number shown for help",
        "option_d": "Screenshot it and search online to check if it's a known scam",
        "outcome_a": "Dangerous. This is a scareware trick — clicking it usually installs the very malware it claims to remove.",
        "outcome_b": "Best choice! Closing it without interacting avoids the trap entirely.",
        "outcome_c": "Dangerous. This connects you directly to scammers posing as tech support.",
        "outcome_d": "Reasonable, but simply closing it (option B) is faster and equally safe.",
        "points_a": 0, "points_b": 10, "points_c": 0, "points_d": 6
    },
    {
        "category": "Safe Browsing & Malware", "icon": "📎",
        "title": "The Suspicious Attachment",
        "story": "You receive an email from an unknown sender with an attachment named 'Result_Slip.docx.scr'.",
        "option_a": "Open it since it mentions your result",
        "option_b": "Don't open it — the '.scr' extension means it's an executable program disguised as a document",
        "option_c": "Open it on a different device to be safe",
        "option_d": "Forward it to a friend to open first",
        "outcome_a": "Dangerous. This is a disguised executable file, likely malware.",
        "outcome_b": "Best choice! Recognizing the double-extension trick protects you from installing hidden malware.",
        "outcome_c": "Still dangerous — the malware risk applies to any device that opens it.",
        "outcome_d": "Dangerous and unfair — this just passes the malware risk on to your friend.",
        "points_a": 0, "points_b": 10, "points_c": 0, "points_d": 0
    },

    # ---------- INCIDENT RESPONSE (2) ----------
    {
        "category": "Incident Response", "icon": "🚨",
        "title": "After Entering Your Password on a Fake Site",
        "story": "You just realized you entered your email password into a link that turned out to be a phishing site.",
        "option_a": "Do nothing and hope they don't use it",
        "option_b": "Immediately change that password (and anywhere else you reused it), and enable MFA",
        "option_c": "Wait a few days to see if anything happens",
        "option_d": "Delete the email account entirely",
        "outcome_a": "Dangerous. Attackers often act quickly once they have a working password.",
        "outcome_b": "Best choice! Fast action across all accounts sharing that password minimizes the damage.",
        "outcome_c": "Risky. Waiting gives an attacker more time to act before you respond.",
        "outcome_d": "Extreme and often impossible — deleting doesn't undo potential data already accessed, and loses your account unnecessarily.",
        "points_a": 0, "points_b": 10, "points_c": 2, "points_d": 3
    },
    {
        "category": "Incident Response", "icon": "🔍",
        "title": "Noticing a Scam Impersonating a Real Company",
        "story": "You spot a fake job posting on Facebook impersonating a real, well-known company, targeting students like you.",
        "option_a": "Ignore it, it's not your problem",
        "option_b": "Report the post to the platform and, if possible, alert the real company",
        "option_c": "Comment publicly warning others in the comment section",
        "option_d": "Share it around yourself to 'expose' the scam",
        "outcome_a": "Missed opportunity. Reporting helps protect others from falling for the same scam.",
        "outcome_b": "Best choice! Official reporting channels are the most effective way to get scam content removed and warn the real company.",
        "outcome_c": "Somewhat helpful, but can tip off scammers to delete and repost elsewhere before it's officially removed.",
        "outcome_d": "Risky — resharing (even to warn) can spread the scam link further to new potential victims.",
        "points_a": 0, "points_b": 10, "points_c": 5, "points_d": 2
    },
]

def seed():
    with app.app_context():
        if Scenario.query.first():
            print("Scenarios already exist. Skipping seeding.")
            return
        for s in scenarios:
            db.session.add(Scenario(**s))
        db.session.commit()
        print(f"Seeded {len(scenarios)} scenarios successfully.")

if __name__ == '__main__':
    seed()