# import re

# def analyze_risks(text):

#     text_lower = text.lower()

#     risk_patterns = {
#         "HIGH": [
#             r"all losses",
#             r"without limitation",
#             r"unlimited liability",
#             r"indemnif\w+",
#             r"held harmless",
#             r"held liable",
#         ],
#         "MEDIUM": [
#             r"terminate anytime",
#             r"without notice",
#             r"no notice",
#             r"immediately",
#             r"penalty",
#             r"fine",
#             r"attorney",
#             r"no refund"
#         ]
#     }

#     risks = []

#     for level, patterns in risk_patterns.items():

#         for pattern in patterns:

#             matches = re.finditer(pattern, text_lower)

#             for match in matches:

#                 start = max(0, match.start()-100)
#                 end = min(len(text), match.end()+100)

#                 clause = text[start:end]

#                 risks.append({
#                     "risk": level,
#                     "pattern": pattern,
#                     "clause": clause
#                 })

#     return risks

import re


def analyze_risks(text):

    text_lower = text.lower()

    risk_patterns = {

        "HIGH": [
            r"all losses",
            r"without limitation",
            r"unlimited liability",
            r"indemnif\w+",
            r"held harmless",
            r"held liable"
        ],

        "MEDIUM": [
            r"terminate anytime",
            r"without notice",
            r"no notice",
            r"immediately",
            r"penalty",
            r"fine",
            r"attorney",
            r"no refund"
        ]
    }

    risks = []

    for level, patterns in risk_patterns.items():

        for pattern in patterns:

            matches = re.finditer(pattern, text_lower)

            for match in matches:

                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)

                clause = text[start:end]

                risks.append({
                    "risk": level,
                    "pattern": pattern,
                    "clause": clause
                })

    return risks