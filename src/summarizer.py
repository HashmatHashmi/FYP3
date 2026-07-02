# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="facebook/bart-large-cnn"
# )

# def summarize_document(chunks):
#     summaries = []

#     for chunk in chunks:

#         input_length = len(chunk.split())

#         max_len = min(120, input_length - 5)
#         min_len = min(30, max_len - 5)

#         summary = summarizer(
#             chunk,
#             max_length=max_len,
#             min_length=max(10, min_len),
#             do_sample=False
#         )[0]["summary_text"]

#         summaries.append(summary)

#     return " ".join(summaries)

from transformers import pipeline


summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_document(chunks):

    summaries = []

    for chunk in chunks:

        input_length = len(chunk.split())

        max_len = min(120, input_length - 5)
        min_len = min(30, max_len - 5)

        summary = summarizer(
            chunk,
            max_length=max_len,
            min_length=max(10, min_len),
            do_sample=False
        )[0]["summary_text"]

        summaries.append(summary)

    return " ".join(summaries)