### Create Interview with Job Description
**Steps:**
1. {'action': 'click', 'selector': '#create-interview-button'}
2. {'action': 'fill', 'selector': '#job-description-input', 'value': 'JavaScript developer with AWS experience'}
3. {'action': 'click', 'selector': '#save-job-description-button'}
**Expected Result:** {'skillRecommendations': True, 'skillSuggestions': ['JavaScript', 'AWS', 'Development']}

### Select Skills from Recommendations
**Steps:**
1. {'action': 'click', 'selector': '#select-skill-button:nth-child(1)'}
2. {'action': 'click', 'selector': '#select-skill-button:nth-child(2)'}
**Expected Result:** {'selectedSkills': ['JavaScript', 'AWS']}

### Configure Question Difficulty Level
**Steps:**
1. {'action': 'select', 'selector': '#question-difficulty-select', 'option': 'Moderate'}
**Expected Result:** {'questionDifficultyLevel': 'Moderate'}

### Add Standard Questions
**Steps:**
1. {'action': 'click', 'selector': '#add-standard-question-button'}
2. {'action': 'fill', 'selector': '#standard-question-input', 'value': "What's the notice period?"}
3. {'action': 'click', 'selector': '#save-standard-question-button'}
**Expected Result:** {'standardQuestions': ["What's the notice period?"]}

### Add Role-Based Questions
**Steps:**
1. {'action': 'click', 'selector': '#add-role-based-question-button'}
2. {'action': 'fill', 'selector': '#role-based-question-input', 'value': "What's your experience with AWS?"}
3. {'action': 'click', 'selector': '#save-role-based-question-button'}
**Expected Result:** {'roleBasedQuestions': ["What's your experience with AWS?"]}

### Create Interview
**Steps:**
1. {'action': 'click', 'selector': '#create-interview-button'}
**Expected Result:** {'interviewCreated': True, 'publicInterviewLink': True}

### View Candidate Responses
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
**Expected Result:** Candidate responses, including video recordings, scores, and resumes, are displayed

### Verify Interview Score
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
2. {'action': 'click', 'target': 'specific candidate response'}
**Expected Result:** Interview score is displayed for the selected candidate

### Verify Communication Score
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
2. {'action': 'click', 'target': 'specific candidate response'}
**Expected Result:** Communication score is displayed for the selected candidate

### Verify AI Summary
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
2. {'action': 'click', 'target': 'specific candidate response'}
**Expected Result:** AI summary, including observations, positives, and negatives, is displayed for the selected candidate

### Select or Reject Candidate
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
2. {'action': 'click', 'target': 'specific candidate response'}
**Expected Result:** Action buttons to select or reject the candidate are displayed

### Upload Resumes for Screening
**Steps:**
1. {'action': 'visit', 'target': '/create-interview'}
2. {'action': 'upload', 'target': 'resume files'}
**Expected Result:** Resumes are successfully uploaded for screening

### View AI Screening Results
**Steps:**
1. {'action': 'visit', 'target': '/screening-results'}
**Expected Result:** AI screening results, including resume scores and recommendations, are displayed

### Send Interview Link to Candidate
**Steps:**
1. {'action': 'visit', 'target': '/screening-results'}
2. {'action': 'click', 'target': 'specific candidate result'}
**Expected Result:** Interview link is sent to the candidate, valid for 24 hours

### View Candidate Interview Submission
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
**Expected Result:** Candidate's interview submission is displayed, including video recording and scores

