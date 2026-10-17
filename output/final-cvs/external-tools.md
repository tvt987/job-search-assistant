# External CV-scoring tools: attempt record

**Result: no external tool was used, so no external score exists.** No score, screenshot or report in this folder comes from Resume Worded, Jobscan or any similar service.

## What was attempted

| Service | Host tested | Result (2026-10-17 08:05 UTC) |
|---|---|---|
| Resume Worded | resumeworded.com | No connection: the host is not allowed by this environment's network policy (DNS failure, HTTP code 000) |
| Jobscan | www.jobscan.co | No connection, same cause |
| Enhancv resume checker | enhancv.com | No connection, same cause |
| TopCV CV review | www.topcv.vn | No connection, same cause |
| ITviec (for live job descriptions) | itviec.com | No connection, same cause |

These services also require a signed-in account and a file upload through a browser. Uploading a CV with personal contact details to a third party is the candidate's decision, and it was not taken here.

## How to get real external scores

**Option A: run them yourself (fastest).**
1. Upload the **ATS** PDF of each track (`CV_*_ATS.pdf`) to Resume Worded's "Score My Resume".
2. In Jobscan, paste the job description of a real posting you plan to apply for. Jobscan scores against one specific job description, not in general.
3. Record the scores and the main findings in this file.

**Option B: allow this environment to reach the hosts.** In the environment settings, open Network access and add the hosts above under Allowed domains. The steps are at <https://code.claude.com/docs/en/cloud-environments#network-access>. Even then the services need a login, which you would have to complete yourself.

## How to read external scores

These tools mostly measure keyword overlap, layout parseability and bullet style; they do not check whether claims are true. A higher Jobscan match obtained by pasting keywords the candidate has not used would make the CV worse. The internal panel scorecard (`cv-scorecard.md`) is a reasoned estimate, not an external measurement.
