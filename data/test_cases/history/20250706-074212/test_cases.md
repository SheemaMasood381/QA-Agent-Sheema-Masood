### Create Interview with Job Description
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests questions based on the job description
**Expected Result:** The interview creation page displays suggested questions based on the job description

### Create Interview with Enhanced JD Feature
**Steps:**
1. Visit the interview creation page
2. Enter a job title (e.g. JavaScript developer with AWS experience)
3. Click on the enhanced JD feature
4. Verify that the AI generates a complete job description
**Expected Result:** The interview creation page displays a generated job description based on the job title

### Edit and Save Job Description
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Edit the job description and click save again
4. Verify that the changes are saved
**Expected Result:** The edited job description is saved and displayed on the interview creation page

### Select Skill Recommendations
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests skill recommendations
4. Select a skill recommendation and verify that it is added to the interview
**Expected Result:** The selected skill recommendation is added to the interview

### Add Custom Skill
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests skill recommendations
4. Add a custom skill and verify that it is added to the interview
**Expected Result:** The custom skill is added to the interview

### Configure Difficulty Level of Questions
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests questions
4. Configure the difficulty level of a question and verify that it is saved
**Expected Result:** The difficulty level of the question is saved and displayed on the interview creation page

### Create Standard Questions
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests standard questions
4. Add a standard question and verify that it is added to the interview
**Expected Result:** The standard question is added to the interview

### Create Role-Based Questions
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests role-based questions
4. Add a role-based question and verify that it is added to the interview
**Expected Result:** The role-based question is added to the interview

### Create Interview with Advanced Plan Features
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests questions
4. Select an AI avatar and verify that it is saved
**Expected Result:** The AI avatar is saved and displayed on the interview creation page

### Create Interview and Get Unique Public Link
**Steps:**
1. Visit the interview creation page
2. Enter a job description and click save
3. Verify that the AI suggests questions
4. Click on the create option and verify that a unique public link is generated
**Expected Result:** A unique public link is generated and displayed on the interview creation page

### Verify Candidate Interview Response
**Steps:**
1. {'action': 'navigate', 'target': 'responses tab'}
2. {'action': 'assert', 'target': "candidate's responses", 'expected': 'structured answers and video recordings along with scores and resumes'}
**Expected Result:** Candidate's responses are displayed with structured answers, video recordings, scores, and resumes

### Verify Interview Score
**Steps:**
1. {'action': 'navigate', 'target': 'responses tab'}
2. {'action': 'assert', 'target': 'interview score', 'expected': 'a numerical score'}
**Expected Result:** Interview score is displayed

### Verify Communication Score
**Steps:**
1. {'action': 'navigate', 'target': 'responses tab'}
2. {'action': 'assert', 'target': 'communication score', 'expected': 'a numerical score'}
**Expected Result:** Communication score is displayed

### Verify AI Analysis Summary
**Steps:**
1. {'action': 'navigate', 'target': 'interview screenings section'}
2. {'action': 'assert', 'target': 'AI analysis summary', 'expected': 'observations, positives, and negatives'}
**Expected Result:** AI analysis summary is displayed with observations, positives, and negatives

### Verify Action Button Functionality
**Steps:**
1. {'action': 'navigate', 'target': 'responses tab'}
2. {'action': 'click', 'target': 'action button'}
3. {'action': 'assert', 'target': 'candidate selection/rejection option', 'expected': 'select or reject the candidate'}
**Expected Result:** Action button allows selecting or rejecting the candidate

### Verify Resume Screening Functionality
**Steps:**
1. {'action': 'navigate', 'target': 'ré screening section'}
2. {'action': 'upload', 'target': 'résumés'}
3. {'action': 'assert', 'target': 'AI screening process', 'expected': 'commences screening process'}
**Expected Result:** Resume screening process commences upon uploading résumés

### Verify AI Ré Score and Recommendation
**Steps:**
1. {'action': 'navigate', 'target': 'ré screening section'}
2. {'action': 'assert', 'target': 'ré score', 'expected': 'a numerical score'}
3. {'action': 'assert', 'target': 'AI recommendation', 'expected': 'candidate recommendation for next stage'}
**Expected Result:** AI ré score and recommendation are displayed

