# from transformers import pipeline

# classifier = pipeline(
#     "zero-shot-classification",
#     model="facebook/bart-large-mnli"
# )

# def classify_document(text):

#     labels = [
#         "legal contract agreement",
#         "property lease agreement",
#         "employment contract",
#         "non disclosure agreement",
#         "memorandum of understanding",
#         "service agreement",
#         "power of attorney",
#         "affidavit",
#         "will and testament",
#         "court judgement",
#         "legal notice",
#         "police complaint",
#         "partnership agreement"
#     ]

#     result = classifier(
#         text,
#         labels,
#         hypothesis_template="This document is a {}."
#     )

#     return {
#         "document_type": result["labels"][0],
#         "confidence": result["scores"][0]
#     }

from transformers import pipeline


classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


def classify_document(text):

    labels = [
        "legal contract agreement",
        "property lease agreement",
        "employment contract",
        "service agreement",
        "non disclosure agreement",
        "memorandum of understanding",
        "power of attorney",
        "affidavit",
        "court judgement",
        "legal notice",
        "police complaint"
    ]

    result = classifier(
        text,
        labels,
        hypothesis_template="This document is a {}."
    )

    return {
        "document_type": result["labels"][0],
        "confidence": result["scores"][0]
    }