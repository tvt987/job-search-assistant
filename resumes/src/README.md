# CV sources have moved

The PDFs in `resumes/` (and the copies in the repository root) are now built by the final pipeline in
[`output/final-cvs/src/`](../../output/final-cvs/src/), which keeps the header-band design of the earlier
version and uses the verified final content.

```bash
python3 output/final-cvs/src/build.py        # designed + ATS-first PDFs; copies the designed ones here
node output/final-cvs/src/build_docx.js      # editable DOCX
python3 output/final-cvs/src/qa.py           # checks the delivered files
```

`assets/headshot.jpg` stays here because the final pipeline uses it for the photo.
The earlier pipeline and its content are in git history (commit `6a11dc4`).
