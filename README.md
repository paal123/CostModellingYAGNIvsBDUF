# Cost Modelling of YAGNI vs BDUF
Cost modelling for YAGNI vs BDUF as base principle for development

Basic probability calculations:

Intersect: A ∩ B

Union: A ∪ B

A but not B: A \ B

Exatcly one of A and B, but not both: A Δ B


Given A independent of B, A ⫫ B

P(A ∩ B) = P(A)P(B)

P(B|A) = P(A ∩ B)/P(A) = P(B)

P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = P(A) + P(B) - P(A)P(B)

P(A \ B) = P(A) - P(A ∩ B) = P(A)-P(A)P(B)

