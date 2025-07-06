### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'selector': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'selector': "button[type='submit']"}
**Expected Result:** AI suggests questions based on the job description

### Customize Standard Questions
**Steps:**
1. {'action': 'click', 'selector': 'div.std-questions'}
2. {'action': 'fill', 'selector': "input[name='stdQuestion1']", 'value': "What's the notice period?"}
3. {'action': 'click', 'selector': "checkbox[preferredAnswer='yes']"}
**Expected Result:** Standard question is updated with preferred answer

### Customize Role-Based Questions
**Steps:**
1. {'action': 'click', 'selector': 'div.role-based-questions'}
2. {'action': 'fill', 'selector': "input[name='roleQuestion1']", 'value': 'Explain your experience with AWS'}
3. {'action': 'click', 'selector': "checkbox[idealAnswer='2 years experience']"}
**Expected Result:** Role-based question is updated with ideal answer

### Create Interview with Customized Questions
**Steps:**
1. {'action': 'click', 'selector': "button[type='create']"}
**Expected Result:** Interview is created with unique public interview link

### Test Interview Link
**Steps:**
1. {'action': 'click', 'selector': "a[href*='public-interview-link']"}
**Expected Result:** Interview link redirects to application form

### Candidate Response View
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
**Expected Result:** Candidate's structured answers, video recordings, scores, and resume are displayed

### Interview Screening Scores
**Steps:**
1. Visit the interview screenings section
2. Click on a candidate's interview
**Expected Result:** AI-analyzed scores, including interview score and communication score, are displayed

### Interview Summary
**Steps:**
1. Visit the interview screenings section
2. Click on a candidate's interview
**Expected Result:** Comprehensive summary of the interview, including observations, positives, and negatives, is displayed

### Select/Reject Candidate
**Steps:**
1. Visit the interview screenings section
2. Click on a candidate's interview
3. Click on the action button
**Expected Result:** Option to select or reject the candidate is available

### Resume Screening
**Steps:**
1. Create an interview
2. Upload multiple resumes
3. Submit for screening
**Expected Result:** AI commences the screening process and assigns a resume score based on skills and job description alignment

### AI Recommendations
**Steps:**
1. Visit the resume screening results
2. Check the AI recommendations
**Expected Result:** AI recommends or rejects candidates based on resume suitability and job description alignment

### Interview Link Sending
**Steps:**
1. Decide to proceed with a candidate
2. Send an interview link to the candidate
**Expected Result:** Candidate receives an interview link valid for 24 hours

### Initiate Interview Screening
**Steps:**
1. Candidate submits their interview
2. Initiate the interview screening process
**Expected Result:** Interview screening summary is available for review

