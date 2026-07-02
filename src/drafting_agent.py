# from transformers import pipeline

# draft_model = pipeline(
#     "text2text-generation",
#     model="google/flan-t5-base"
# )

# def drafting_agent(clause, risk_level):

#     prompt = f"""
# You are an expert legal assistant.

# Rewrite ONLY the clause below.

# Requirements:
# - Keep the same meaning.
# - Reduce legal risk.
# - Use professional legal language.
# - Return only the revised clause.
# - Do NOT explain anything.
# - Do NOT number the answer.

# Risk Level:
# {risk_level}

# Clause:
# {clause}

# Revised Clause:
# """

#     result = draft_model(
#         prompt,
#         max_length=150,
#         do_sample=False
#     )

#     return result[0]["generated_text"].strip()


from transformers import pipeline


draft_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def drafting_agent(clause, risk_level):

    prompt = f"""
You are an expert legal drafting assistant.

Rewrite ONLY the following legal clause.

Requirements:
- Preserve meaning.
- Reduce legal risk.
- Use professional legal language.
- Return only the revised clause.

Risk Level:
{risk_level}

Clause:
{clause}

Revised Clause:
"""

    result = draft_model(
        prompt,
        max_length=150,
        do_sample=False
    )

    return result[0]["generated_text"].strip()