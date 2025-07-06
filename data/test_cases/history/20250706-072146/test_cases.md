### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Select Skills from AI Recommendations
**Steps:**
1. {'action': 'click', 'target': "li[data-skill='AWS']"}
2. {'action': 'click', 'target': "li[data-skill='JavaScript']"}
**Expected Result:** Selected skills are added to the interview creation process

### Choose Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'target': "select[name='difficultyLevel']", 'value': 'Moderate'}
**Expected Result:** Difficulty level is updated for the interview questions

### View Standard and Role-Based Questions
**Steps:**
1. {'action': 'click', 'target': "button[title='Expand standard questions']"}
2. {'action': 'click', 'target': "button[title='Expand role-based questions']"}
**Expected Result:** Both standard and role-based questions are displayed

### Customize Questions
**Steps:**
1. {'action': 'click', 'target': "input[name='question']"}
2. {'action': 'type', 'target': "input[name='question']", 'value': 'What is your experience with AWS?'}
3. {'action': 'click', 'target': "input[name='idealAnswer']"}
4. {'action': 'type', 'target': "input[name='idealAnswer']", 'value': '2+ years'}
**Expected Result:** Custom question is added to the interview

### Create Interview with Selected Questions
**Steps:**
1. {'action': 'click', 'target': "button[type='submit']"}
**Expected Result:** Interview is created successfully and a unique public interview link is generated

### Verify Public Interview Link
**Steps:**
1. {'action': 'verify', 'target': 'text=Public Interview Link'}
**Expected Result:** Public interview link is displayed

### Verify candidate's interview score and communication score
**Steps:**
1. {'description': 'Open the responses tab', 'action': 'click', 'selector': 'text=Responses'}
2. {'description': "Select the candidate's video interview", 'action': 'click', 'selector': 'video-interview-link'}
**Expected Result:** {'interview_score': 'greater than 0', 'communication_score': 'greater than 0'}

### Verify AI comprehensive summary of the interview
**Steps:**
1. {'description': 'Open the responses tab', 'action': 'click', 'selector': 'text=Responses'}
2. {'description': "Select the candidate's video interview", 'action': 'click', 'selector': 'video-interview-link'}
**Expected Result:** {'summary': 'contains observations, positives, and negatives'}

### Verify action buttons to select or reject the candidate
**Steps:**
1. {'description': 'Open the responses tab', 'action': 'click', 'selector': 'text=Responses'}
2. {'description': "Select the candidate's video interview", 'action': 'click', 'selector': 'video-interview-link'}
**Expected Result:** {'action_buttons': ['Select', 'Reject']}

### Verify ré screening functionality
**Steps:**
1. {'description': 'Create an interview and upload resumes', 'action': 'upload', 'selector': 'resume-upload-input'}
2. {'description': 'Submit the resumes for screening', 'action': 'click', 'selector': 'submit-resumes-button'}
**Expected Result:** {'ré_scores': 'array of scores', 'AI_recommendations': 'array of recommendations'}

### Verify semantic analysis and ré score assignment
**Steps:**
1. {'description': 'Open the ré screening results', 'action': 'click', 'selector': 'ré-screening-results-link'}
**Expected Result:** {'semantic_analysis': 'conducted', 'ré_score': 'greater than 0'}

### Verify AI recommendation for the next stage
**Steps:**
1. {'description': 'Open the ré screening results', 'action': 'click', 'selector': 'ré-screening-results-link'}
**Expected Result:** {'AI_recommendation': 'boolean', 'reason': 'string'}

