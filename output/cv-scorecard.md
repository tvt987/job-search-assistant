# CV scorecard

All scores below are **internal panel estimates**. Independent reviewer agents produced them, each playing recruiter, hiring manager, ATS specialist, designer and fact-checker. The reviewers read the real PDF and DOCX files, extracted their text and checked each claim against the public repos.

They are **not external measurements**. No CV-scoring website could be reached (see `final-cvs/external-tools.md`), and a score from a different reviewer or tool will differ.

## Rubric

| Criterion | Points | What earns them |
|---|---|---|
| Targeting | 15 | Title, keyword line and summary match the role. The most relevant evidence comes first. |
| Technical evidence | 15 | Concrete, checkable work: linked repos whose code matches the bullets. |
| Achievements / impact | 15 | Results and outcomes, not only duties or counts. |
| JD relevance | 15 | Coverage of what HCMC postings ask for (see `market-research.md`). |
| ATS compatibility | 15 | Text extracts in reading order with standard headings, exact keyword forms and no broken characters. |
| Visual design / readability | 10 | Hierarchy, contrast, font size, density, no widows. |
| Grammar / clarity | 5 | Clear, consistent English. |
| Differentiation | 5 | What makes this candidate memorable. |
| Consistency | 5 | Dates, titles and claims agree within the CV and with the public profile. |

**Factual accuracy** is scored separately. 100% means every claim is supported by the verified facts or the repos.

## Results (designed version)

| Track | Original (git `5e8e9db`) | Round 1 | Round 2 | Round 3 (final measured) |
|---|---|---|---|---|
| Backend .NET | **63** · factual ~85% | 80 · ~94% | 83 · ~96% | **87 · 98%** |
| Full Stack .NET + Angular | **65** · factual ~89% | 75 · ~92% | 82 · ~95% | **86 · 99%** |
| AI Application Engineer | **60** · factual ~78% | 80 · ~94% | 84 · ~95% | **88 · 98%** |

The ATS-first versions score **14/15 on ATS** for all three tracks; the designed versions score 14/15 in round 3.

**Round 4** fixed the last minor items reviewers found: wording restored from the originals, "contact-data masking", "market intelligence", grammar and widow lines. It was **not re-scored**. The round-3 reviewer estimated about +1 point per track for these fixes. That estimate is not counted above.

## Round-3 breakdown

| Criterion | Backend | Full Stack | AI |
|---|---|---|---|
| Targeting /15 | 14 | 14 | 14 |
| Technical evidence /15 | 13 | 13 | 14 |
| Achievements /15 | 10 | 10 | 10 |
| JD relevance /15 | 14 | 14 | 13 |
| ATS /15 | 14 | 14 | 14 |
| Visual /10 | 9 | 8 | 9 |
| Grammar /5 | 4 | 4 | 4 |
| Differentiation /5 | 4 | 4 | 5 |
| Consistency /5 | 5 | 5 | 5 |
| **Total** | **87** | **86** | **88** |

## Why the target of 95 was not reached

Reviewers in rounds 2 and 3 independently put the ceiling without new facts at about **87–90**. Three criteria cannot be raised by wording without inventing facts:

- **Achievements (10/15).** No business-impact figure from Con Cung exists. The candidate chose not to estimate one, and inventing one is prohibited.
- **Technical evidence (13–14/15).** Several things cap it:
  - The Retail Reliability Lab has no public repo.
  - The Partner Integration BFF has no CI.
  - The RAG evaluation gates CI only on the offline pipeline.
  - Ecommerce-Admin and Layout-Store are shared codebases.
- **Targeting.** The real job title is "Full Stack Developer", and the Angular 19 work sits in projects until the candidate says where it was done.

The stopping rule was met:
- Round 3 had no critical or major findings.
- The reviewer judged that no wording-only change could add 2 or more points.
- Round 4 (minor fixes) produced no material gain.

`next-improvements.md` lists the evidence that would move each capped criterion.

## Baseline note: the CVs in `resumes/`

Before this task, `resumes/` held a redesigned set (commit `6a11dc4`) built earlier in this conversation. These are not the originals. That set has a **critical ATS defect**:
- Bullets are painted after the normal text flow, so a stream-order parser (pypdf) sees an empty "WORK EXPERIENCE" section and the bullets at the end of the page.
- Its headings extract letter-spaced ("W O R K  E X P E R I E N C E").

It also kept the unsupported Support Ticket numbers. It was not scored. Use the files in `final-cvs/` instead.
