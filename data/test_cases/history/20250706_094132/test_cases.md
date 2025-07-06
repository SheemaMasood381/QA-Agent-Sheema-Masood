### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': '2-year experienced JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** AI suggests questions based on the job description

### Verify Skill Recommendations
**Steps:**
1. {'action': 'waitForSelector', 'target': 'div.skills-recommendations'}
2. {'action': 'assert', 'target': 'div.skills-recommendations', 'expected': 'Key skills extracted from the job description'}
**Expected Result:** Skill recommendations displayed

### Select Standard Questions
**Steps:**
1. {'action': 'click', 'target': 'div.standard-questions'}
2. {'action': 'assert', 'target': 'div.standard-questions', 'expected': 'Objective questions displayed'}
**Expected Result:** Standard questions displayed

### Customize Question Options
**Steps:**
1. {'action': 'click', 'target': 'div.question-option'}
2. {'action': 'fill', 'target': "input[name='preferredAnswer']", 'value': '30 days'}
3. {'action': 'assert', 'target': 'div.question-option', 'expected': 'Preferred answer saved'}
**Expected Result:** Preferred answer saved

### Create Interview with Selected Questions
**Steps:**
1. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Interview created successfully

### Verify Public Interview Link
**Steps:**
1. {'action': 'assert', 'target': 'div.public-interview-link', 'expected': 'Unique public interview link displayed'}
**Expected Result:** Public interview link displayed

### Viewing candidate responses
**Steps:**
1. Navigate to the responses tab
2. Click on a candidate's response
**Expected Result:** The candidate's structured answers, video recordings, scores, and resume are displayed

### Viewing interview scores
**Steps:**
1. Navigate to the interview screenings section
2. Click on a candidate's interview
**Expected Result:** The candidate's interview score and communication score are displayed

### Viewing AI analysis scores
**Steps:**
1. Navigate to the interview screenings section
2. Click on a candidate's interview
**Expected Result:** The AI analysis scores, including observations, positives, and negatives, are displayed

### Selecting or rejecting a candidate
**Steps:**
1. Navigate to the interview screenings section
2. Click on a candidate's interview
3. Click the action button
**Expected Result:** The option to select or reject the candidate is available

### Uploading resumes for screening
**Steps:**
1. Create an interview
2. Upload multiple resumes
**Expected Result:** The resumes are uploaded successfully and the AI commences the screening process

### Viewing resume screening results
**Steps:**
1. Navigate to the resume screening section
2. Click on a candidate's resume
**Expected Result:** The candidate's resume score and AI recommendation are displayed

### Sending an interview link to a candidate
**Steps:**
1. Navigate to the resume screening section
2. Click on a candidate's resume
3. Click the 'Send Interview Link' button
**Expected Result:** The interview link is sent to the candidate and is valid for 24 hours

### Viewing candidate interview submission
**Steps:**
1. Navigate to the responses tab
2. Click on a candidate's response
**Expected Result:** The candidate's interview submission is displayed, including video recordings and scores

