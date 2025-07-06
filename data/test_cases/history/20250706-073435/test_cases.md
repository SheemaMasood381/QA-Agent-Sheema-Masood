### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** {'skillRecommendationsVisible': True}

### Select Skills from AI Recommendations
**Steps:**
1. {'action': 'check', 'target': "checkbox[name='skill1']"}
2. {'action': 'check', 'target': "checkbox[name='skill2']"}
**Expected Result:** {'selectedSkillsCount': 2}

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'target': "select[name='difficultyLevel']", 'value': 'moderate'}
**Expected Result:** {'difficultyLevelSelected': 'moderate'}

### Create Interview with Standard Questions
**Steps:**
1. {'action': 'check', 'target': "checkbox[name='standardQuestion1']"}
2. {'action': 'check', 'target': "checkbox[name='standardQuestion2']"}
**Expected Result:** {'standardQuestionsCount': 2}

### Create Interview with Role-Based Questions
**Steps:**
1. {'action': 'check', 'target': "checkbox[name='roleBasedQuestion1']"}
2. {'action': 'check', 'target': "checkbox[name='roleBasedQuestion2']"}
**Expected Result:** {'roleBasedQuestionsCount': 2}

### Create Interview with Custom Questions
**Steps:**
1. {'action': 'fill', 'target': "input[name='customQuestion']", 'value': 'What is your experience with JavaScript?'}
**Expected Result:** {'customQuestionVisible': True}

### Create Interview and Verify Unique Public Link
**Steps:**
1. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** {'uniquePublicLinkVisible': True}

### Can view candidate's responses
**Steps:**
1. {'action': 'visit', 'target': 'responses tab'}
2. {'action': 'view', 'target': 'structured answers and video recordings'}
3. {'action': 'view', 'target': 'scores and resumes'}
**Expected Result:** Candidate's responses are visible

### Can view AI analyze scores
**Steps:**
1. {'action': 'visit', 'target': 'interview screenings section'}
2. {'action': 'view', 'target': 'AI analyze scores'}
**Expected Result:** AI analyze scores are visible

### Can view comprehensive summary of the interview
**Steps:**
1. {'action': 'view', 'target': 'interview summary'}
2. {'action': 'view', 'target': 'observations, positives, and negatives'}
**Expected Result:** Comprehensive summary of the interview is visible

### Can select or reject candidate
**Steps:**
1. {'action': 'click', 'target': 'action button'}
2. {'action': 'select', 'target': 'select or reject option'}
**Expected Result:** Candidate is selected or rejected

### Can upload resumes for screening
**Steps:**
1. {'action': 'create', 'target': 'interview'}
2. {'action': 'upload', 'target': 'resumes'}
**Expected Result:** Resumes are uploaded for screening

### Can view AI recommended profiles
**Steps:**
1. {'action': 'view', 'target': 'AI recommended profiles'}
2. {'action': 'view', 'target': 'ré score'}
**Expected Result:** AI recommended profiles are visible

### Can decide to reject or advance candidate
**Steps:**
1. {'action': 'view', 'target': 'AI recommendation'}
2. {'action': 'decide', 'target': 'reject or advance candidate'}
**Expected Result:** Can make a decision on the candidate

### Can send interview link to candidate
**Steps:**
1. {'action': 'send', 'target': 'interview link'}
2. {'action': 'validate', 'target': 'interview link is valid for 24 hours'}
**Expected Result:** Interview link is sent to candidate and is valid for 24 hours

