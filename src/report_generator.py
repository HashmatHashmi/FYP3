# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet

# def generate_report(document_type, confidence, summary, risks):

#     report = "\n========== LEGAL DOCUMENT ANALYSIS REPORT ==========\n\n"

#     report += f"Document Type : {document_type}\n"
#     report += f"Confidence    : {confidence:.2f}\n\n"

#     report += "--------------- SUMMARY ---------------\n"
#     report += summary + "\n\n"

#     report += "------------- RISK ANALYSIS ------------\n"

#     if risks:
#         for risk in risks:


#             report += f"Risk Level : {risk['risk']}\n"

#             report += f"Detected Clause:\n{risk['clause']}\n\n"

#             safer_clause = drafting_agent(
#                 risk["clause"],
#                 risk["risk"]
#             )

#             report += "Suggested Revision:\n"

#             report += safer_clause

#             report += "\n"

#             report += "-"*60 + "\n"

#     else:
#         report += "No risks detected.\n"

#     report += "\n===============================================\n"

#     return report


# def save_report_txt(report, filename="reports/legal_analysis_report.txtx"):

#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(report)

#     print(f"Report saved as: {filename}")


from src.drafting_agent import drafting_agent


def generate_report(document_type,
                    confidence,
                    summary,
                    risks):

    report = ""

    report += "=" * 60 + "\n"
    report += "LEGAL DOCUMENT ANALYSIS REPORT\n"
    report += "=" * 60 + "\n\n"

    report += f"Document Type : {document_type}\n"
    report += f"Confidence    : {confidence:.2f}\n\n"

    report += "SUMMARY\n"
    report += "-" * 60 + "\n"
    report += summary + "\n\n"

    report += "RISK ANALYSIS\n"
    report += "-" * 60 + "\n"

    if risks:

        for risk in risks:

            report += f"\nRisk Level : {risk['risk']}\n\n"

            report += "Detected Clause:\n"

            report += risk["clause"] + "\n\n"

            safer = drafting_agent(
                risk["clause"],
                risk["risk"]
            )

            report += "Suggested Revision:\n"

            report += safer + "\n"

            report += "\n" + "-" * 60 + "\n"

    else:

        report += "No significant risks detected.\n"

    return report


def save_report(report,
                filename="reports/legal_analysis_report.txt"):

    with open(filename,
              "w",
              encoding="utf-8") as f:

        f.write(report)