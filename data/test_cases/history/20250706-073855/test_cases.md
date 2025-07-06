### Create an Interview with Job Description
**Steps:**
1. {'step': 'Goto the Interview Creation Page', 'action': 'goto', 'target': 'https://example.com/create-interview'}
2. {'step': 'Enter Job Description', 'action': 'fill', 'target': "input[name='jobDescription']", 'value': '2-year experienced JavaScript developer with AWS experience'}
3. {'step': 'Click Save Job Description', 'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Select Skills from AI Recommendations
**Steps:**
1. {'step': 'Wait for Skill Recommendations to Load', 'action': 'waitForSelector', 'target': '.skill-recommendations'}
2. {'step': 'Select a Skill', 'action': 'click', 'target': '.skill-recommendations li:nth-child(1) .select-skill'}
**Expected Result:** Selected skill is displayed in the skills list

### Customize Questions with Preferred Answers
**Steps:**
1. {'step': 'Wait for Questions to Load', 'action': 'waitForSelector', 'target': '.questions-list'}
2. {'step': 'Edit a Question', 'action': 'click', 'target': '.questions-list li:nth-child(1) .edit-question'}
3. {'step': 'Select a Preferred Answer', 'action': 'click', 'target': '.preferred-answer-options li:nth-child(1)'}
**Expected Result:** Preferred answer is saved for the question

### Create an Interview with Customized Questions
**Steps:**
1. {'step': 'Click Create Interview', 'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Interview is created with a unique public interview link

### Viewing candidate responses
**Steps:**
1. {'action': 'navigate', 'target': 'responses tab'}
2. {'action': 'expect', 'target': 'structured answers, video recordings, scores, and resumes'}
**Expected Result:** User can view candidate responses

### Viewing interview scores
**Steps:**
1. {'action': 'navigate', 'target': 'interview screenings section'}
2. {'action': 'expect', 'target': 'AI analyze scores'}
**Expected Result:** User can view interview scores

### Viewing communication score
**Steps:**
1. {'action': 'navigate', 'target': 'interview screenings section'}
2. {'action': 'expect', 'target': 'communication score'}
**Expected Result:** User can view communication score

### Viewing comprehensive interview summary
**Steps:**
1. {'action': 'navigate', 'target': 'interview screenings section'}
2. {'action': 'expect', 'target': 'comprehensive summary of interview, noting observations, positives, and negatives'}
**Expected Result:** User can view comprehensive interview summary

### Selecting or rejecting a candidate
**Steps:**
1. {'action': 'click', 'target': 'action button (select or reject)'}
2. {'action': 'expect', 'target': 'candidate selection or rejection confirmed'}
**Expected Result:** User can select or reject a candidate

### Uploading resumes for screening
**Steps:**
1. {'action': 'navigate', 'target': 'upload resumes section'}
2. {'action': 'upload', 'target': 'resumes to be screened'}
**Expected Result:** User can upload resumes for screening

### Viewing AI screening results
**Steps:**
1. {'action': 'navigate', 'target': 'screening results section'}
2. {'action': 'expect', 'target': 'AI screening results, including ré score and recommendation'}
**Expected Result:** User can view AI screening results

### Sending interview link to candidate
**Steps:**
1. {'action': 'click', 'target': 'send interview link button'}
2. {'action': 'expect', 'target': 'interview link sent to candidate'}
**Expected Result:** User can send interview link to candidate

