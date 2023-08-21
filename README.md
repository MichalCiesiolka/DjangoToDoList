# Django To-Do List
## About the project
The Django To-Do List project aims to provide a task management system with user authentication and authorization. Users can create, manage, and track their tasks, with task details including ID, name, description, creator, deadline, creation timestamp, and finish timestamp when a task is marked as finished. Additionally, tasks can be organized into two categories: active and finished. Active tasks are tasks that are awaiting completion, while finished tasks are those that have been successfully completed.

## Project Features:

### User Authentication and Authorization:
- Users can register and log in to their accounts.
- Authentication ensures that only logged-in users can access the task management features.
- Access to tasks is restricted based on the creator's identity and administrator privileges.

### Task Management:
- Users can create, update, delete, and finish tasks.
- Tasks contain the following attributes:
	ID: A unique identifier for each task.
	Name: A brief title or headline for the task.
	Description: Additional details or instructions related to the task.
	Creator: The user who created the task.
	Finish Until: The deadline by which the task should be completed.
	Created At: Timestamp indicating when the task was created.
	Finished At: Timestamp indicating when the task was marked as finished.

### Task Organization:
- Users can view a list of active and finished tasks.
- Users can restore a finished task to its unfinished state.
- Users can edit task name, description and deadline when a task should be finished.

### Admin Access:
- Administrators have special privileges to manage all tasks regardless of the creator.
- Admins can view, edit, and delete all tasks.