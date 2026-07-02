# def legal_document_analysis(pdf_path):

#     # Step 1: Extract Text
#     raw_text = extract_text_from_pdf(pdf_path)

#     # Step 2: Clean Text
#     cleaned_text = clean_text(raw_text)

#     # Step 3: Chunk Text
#     chunks = chunk_text(cleaned_text)

#     # Step 4: Summarize
#     summary = summarize_document(chunks)

#     # Step 5: Classify
#     document_info = classify_document(cleaned_text)

#     # Step 6: Risk Analysis
#     risks = analyze_risks(cleaned_text)

#     # Step 7: Generate Report
#     report = generate_report(
#         document_info["document_type"],
#         document_info["confidence"],
#         summary,
#         risks
#     )

#     save_report_txt(report)

#     return report