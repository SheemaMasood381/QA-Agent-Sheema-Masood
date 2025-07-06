### Create Interview with Job Description
**Steps:**
1. {'action': 'click', 'target': 'input#jobDescription'}
2. {'action': 'fill', 'target': 'input#jobDescription', 'value': '2-year experienced JavaScript developer with AWS experience'}
3. {'action': 'click', 'target': 'button#saveJobDescription'}
**Expected Result:** {'visibility': 'visible', 'elements': ['#skillRecommendations', '#standardQuestions', '#roleBasedQuestions']}

### Select Skills and Set Difficulty Level
**Steps:**
1. {'action': 'click', 'target': 'checkbox#awsSkill'}
2. {'action': 'select', 'target': 'select#difficultyLevel', 'value': 'hard'}
**Expected Result:** {'visibility': 'visible', 'elements': ['#standardQuestions', '#roleBasedQuestions']}

### Customize Standard Questions
**Steps:**
1. {'action': 'click', 'target': 'input#standardQuestion1'}
2. {'action': 'fill', 'target': 'input#standardQuestion1', 'value': "What's the notice period?"}
3. {'action': 'check', 'target': 'checkbox#preferredAnswer1'}
**Expected Result:** {'visibility': 'visible', 'elements': ['#standardQuestions', '#roleBasedQuestions']}

### Customize Role-Based Questions
**Steps:**
1. {'action': 'click', 'target': 'input#roleBasedQuestion1'}
2. {'action': 'fill', 'target': 'input#roleBasedQuestion1', 'value': 'How do you handle AWS errors?'}
3. {'action': 'check', 'target': 'checkbox#idealAnswer1'}
**Expected Result:** {'visibility': 'visible', 'elements': ['#standardQuestions', '#roleBasedQuestions']}

### Create Interview
**Steps:**
1. {'action': 'click', 'target': 'button#createInterview'}
**Expected Result:** {'visibility': 'visible', 'elements': ['#uniquePublicInterviewLink']}

### View candidate responses
**Steps:**
1. Navigate to the responses tab
2. Click on a candidate's response to view their video interview and structured answers
3. Verify that the candidate's score, resume, and video recording are displayed
**Expected Result:** The candidate's response is displayed with their score, resume, and video recording

### View detailed scoring
**Steps:**
1. Navigate to the interview screenings section
2. Click on a candidate's interview to view their AI-analyzed scores
3. Verify that the AI provides a comprehensive summary of the interview, including observations, positives, and negatives
**Expected Result:** The detailed scoring page displays the AI's analysis of the candidate's interview

### Take action on a candidate
**Steps:**
1. Navigate to the responses tab
2. Click on a candidate's response
3. Verify that an action button is displayed to either select or reject the candidate
**Expected Result:** The action button is displayed, allowing the user to select or reject the candidate

### Screen resumes against a job description
**Steps:**
1. Create an interview and upload a set of resumes
2. Verify that the AI commences the screening process
3. Verify that each resume is assigned a score based on the candidate's skills and experience
**Expected Result:** The AI screens the resumes and assigns a score to each, indicating the candidate's suitability for the job

### View AI recommendations
**Steps:**
1. Navigate to the resume screening results
2. Verify that the AI provides a recommendation for each candidate, indicating whether they are suitable for the next stage
**Expected Result:** The AI recommendations are displayed, indicating whether each candidate is suitable for the next stage

### Send interview link to candidate
**Steps:**
1. Select a candidate to advance to the next round
2. Verify that an interview link is sent to the candidate, valid for 24 hours
3. Verify that the candidate can submit their interview at their convenience
**Expected Result:** The interview link is sent to the candidate, allowing them to submit their interview

