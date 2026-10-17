# Next improvements (need the candidate)

The final CVs reached the limit of what wording alone can do with the verified facts. Every reviewer in rounds 2 and 3 put the ceiling without new facts at about 87–90/100. The items below are the evidence that would raise the scores. They are ordered by expected gain. None of them may be guessed or invented.

## Top 5 evidence items

| # | Evidence to add | Why it matters | Expected gain | Where it goes |
|---|---|---|---|---|
| 1 | **One or two real impact figures from Con Cung.** Examples: vouchers or batches created per month with the tool you built; number of admin users or stores; time saved by the code-template tool; defects fixed; team size and your role (module owner, reviewer). | Achievements is stuck at 9/15 on all three CVs because every number is a count of work items, not a result. Recruiters weight this criterion most. | +3 to +5 on each CV | First two Con Cung bullets |
| 2 | **Where the Angular 19 work was done.** Ecommerce-Admin and Layout-Store use Con Cung (`CCI.*`) namespaces. If you built those screens as part of your job, they belong under Con Cung, not under Projects. | Full Stack targeting: today the CV reads as "AngularJS at work, modern Angular on the side". Postings ask for 2+ years of Angular 12–15+. Also check that publishing these codebases does not breach your employment contract. | +2 to +3 (Full Stack) | Work experience |
| 3 | **Publish the corrected GitHub profile README** (`github-profile/README.md`) to `tvt987/tvt987`. | The CVs link github.com/tvt987. The current profile shows different dates, internships and school (Con Cung from 07/2024, FPT Polytechnic). A hiring manager who compares the two will doubt the CV. | Avoids rejection | GitHub |
| 4 | **Add CI to Partner Integration BFF** (a GitHub Actions workflow that runs the 42 xUnit tests). Also **run the RAG evaluation once against a real LLM** and commit the results. | The BFF claims are true but nothing runs the tests publicly. The RAG evaluation currently gates CI only on the offline extractive pipeline, so it says nothing about how a real model behaves. | +1 to +2 (Backend, AI) | BFF and RAG bullets |
| 5 | **Set an ASCII LinkedIn URL**, e.g. `linkedin.com/in/truongvantinh`. | The current address contains Vietnamese diacritics, which many ATS and older Vietnamese job portals mangle. | +1 on ATS | CV header, all three tracks |

## Other open points

- **Retail Reliability Lab has no public repo.**
  - Publish it, or keep the "AI-assisted lab, no public repo" label.
  - Prepare to explain the 3.63 → 0.005 ms result (what changed: an index? an in-process cache?). An interviewer will ask.
- **Employment type.** You graduated in 2026 and have worked at Con Cung since 11/2023. If that was full-time while studying, writing "(full-time)" removes a likely recruiter question.
- **Linux, cloud and production deployment.**
  - These appear often in AI and backend postings.
  - They are not claimed anywhere, because they are not confirmed.
  - If you have real experience, provide it.
- **English.** Some multinational postings filter for spoken English. A recognised score (IELTS/TOEIC) would open those roles. There is no certificate today and none is claimed.
- **Support Ticket validation numbers** (10 HTTP scenarios, 120/720 cases, 1,000 decisions).
  - These were removed because the public repo does not contain them.
  - Commit the scripts that produce them and the numbers can be restored.

## Application-time inputs (do not guess)

These are `NEEDS_USER_INPUT` in the job tracker, not CV content:
- Salary expectation.
- Notice period or earliest start date.
- Work authorisation.
- Relocation.
- Any legal declarations.
