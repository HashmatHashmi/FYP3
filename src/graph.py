# class AgentState(TypedDict):

#     pdf_path: str

#     raw_text: str

#     cleaned_text: str

#     chunks: list

#     summary: str

#     document_type: str

#     confidence: float

#     risks: list

#     report: str

# def extraction_node(state):

#     raw_text = extract_text_from_pdf(state["pdf_path"])

#     return {
#         "raw_text": raw_text
#     }

# def cleaning_node(state):

#     cleaned_text = clean_text(
#         state["raw_text"]
#     )

#     chunks = chunk_text(
#         cleaned_text
#     )

#     return {
#         "cleaned_text": cleaned_text,
#         "chunks": chunks
#     }

# def summarizer_node(state):

#     summary = summarize_document(
#         state["chunks"]
#     )

#     return {
#         "summary": summary
#     }

# def classifier_node(state):

#     result = classify_document(
#         state["cleaned_text"]
#     )

#     return {
#         "document_type": result["document_type"],
#         "confidence": result["confidence"]
#     }

# def risk_node(state):

#     risks = analyze_risks(
#         state["cleaned_text"]
#     )

#     return {
#         "risks": risks
#     }

# def report_node(state):

#     report = generate_report(
#         state["document_type"],
#         state["confidence"],
#         state["summary"],
#         state["risks"]
#     )

#     return {
#         "report": report
#     }

# graph = StateGraph(AgentState)

# graph.add_node(
#     "extractor",
#     extraction_node
# )

# graph.add_node(
#     "cleaner",
#     cleaning_node
# )

# graph.add_node(
#     "summarizer",
#     summarizer_node
# )

# graph.add_node(
#     "classifier",
#     classifier_node
# )

# graph.add_node(
#     "risk",
#     risk_node
# )

# graph.add_node(
#     "report",
#     report_node
# )

# graph.set_entry_point(
#     "extractor"
# )

# graph.add_edge(
#     "extractor",
#     "cleaner"
# )

# graph.add_edge(
#     "cleaner",
#     "summarizer"
# )

# graph.add_edge(
#     "summarizer",
#     "classifier"
# )

# graph.add_edge(
#     "classifier",
#     "risk"
# )

# graph.add_edge(
#     "risk",
#     "report"
# )

# graph.add_edge(
#     "report",
#     END
# )
