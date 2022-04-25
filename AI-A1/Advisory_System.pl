% Made advisory system for Mtech and Btech level stream selection based on some question asked to students/users.
% System will recommend the best suitable stream for user based on user_responses,
% if it is not able to found suitable stream simply returns false in that case.
% Running this program simply consult the file in prolog and then type systems.
% then please respond to some question in option you just need to type option like 0. or 1.
% I have  taking input in options format, so that user is familiar with the options and choice can be made for asked question.

% starting of program
% it will calls different function and determine the suitable stream based on the user response and
% also suggest some career path user can take after completion of the particular stream/course.

systems :-
  start,
  reset_user_responses,
  find_stream(Stream).

start :-
  write('In which stream sholud I pursue in my B.Tech or M.Tech?'), nl,
  write('Kindly answer some questions so that I can suggest you suitable stream based on your response and interest'), nl.

% function for finding the suitable stream for student when he respond to some questions asked
find_stream(Stream) :-
  stream(Stream), !.

% Store user_response to track progress of the user
:- dynamic(progress/2).

% this function will reset the stored user_progress
% reset_user_responses must always return true,but retract function can return true or false
% so, avoid the situation fail if it returns false we will go with second
reset_user_responses :-
  retract(progress(_, _)),
  fail.
reset_user_responses.

%btech_streams
% Btech_stream finding, it will asks some question to you and give the suitable response according to your answer
% function called for different program like cse,it,ece,me etc.

stream(computer_science) :-
  btech_or_mtech(btech),
  computer_systems(yes),
  computer_or_manually(computer),
  (better_in_solving_problem(solving_problem)),
  work_with_numbers(yes),
  (technology(develop);technology(apply)),
  maths(yes),
  deal_with_circuits(no),
  (chemistry(yes);chemistry(no)),
  (physics(yes);physics(no)),
  (biology(yes);biology(no)),
  write('Recommendation: Computer Science '),nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Software Engineer'),nl,
  write('- System Engineer'),nl,
  write('- App Developer'),nl,
  write('- Game Developer'),nl,
  write('- Network Specialist'),nl,
  write('- Researcher'),nl,
  write('- Software Quality Assurance Engineer'),nl.

stream(information_technology) :-
  btech_or_mtech(btech),
  computer_systems(yes),
  computer_or_manually(computer),
  (better_in_solving_problem(solved_problem_as_application)),
  (work_with_numbers(yes);work_with_numbers(no)),
  technology(apply),
  maths(yes),
  deal_with_circuits(no),
  (chemistry(yes);chemistry(no)),
  (physics(yes);physics(no)),
  (biology(yes);biology(no)),
  write('Recommendation: Information Technology '),nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
 write('- Network Administrator'),nl,
  write('- Computer Support Specialist'),nl,
  write('- Information Technology Manager'),nl,
  write('- Database Administrator'),nl,
  write('- System Administrator'),nl,
  write('- Information Systems Manager.'),nl.

stream(electronic_engineering) :-
  btech_or_mtech(btech),
  computer_systems(no),
  computer_or_manually(manually),
  better_in_solving_problem(solving_problem),
  (work_with_numbers(yes);work_with_numbers(no)),
  technology(apply),
  maths(yes),
  deal_with_circuits(yes),
  (chemistry(yes);chemistry(no)),
  (physics(yes);physics(no)),
  (biology(yes);biology(no)),
  write('Recommendation: Electrical/Electronic Engineering '),
  nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Electrical or Electronic Engineer'),nl,
  write('- Technical Director'),nl,
  write('- Network Planning Engineer'),
  write('- Desktop Support Engineer'),nl,
  write('- Electronics Device and Development Engineer').

stream(mechanical_engineering) :-
  btech_or_mtech(btech),
  computer_systems(no),
  computer_or_manually(manually),
  better_in_solving_problem(solved_problem_as_application),
  work_with_numbers(yes),
  maths(yes),
  deal_with_circuits(no),
  (chemistry(yes);chemistry(no)),
  (physics(yes)),
  (biology(yes);biology(no)),
  write('Recommendation: Mechanical Engineering '),
  nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Mechanical Engineer'),nl,
  write('- Production Engineer'),nl,
  write('- Failure Analyst Engineer'),nl,
  write('- M&E Engineer'),nl,
  write('- QC Engineer'),nl,
  write('- Manufacturing Engineer'),nl,
  write('- R&D Engineer'),nl,
  write('- Design Engineer'),nl,
  write('- Product Engineer').

stream(chemical_engineering) :-
  btech_or_mtech(btech),
  computer_systems(no),
  computer_or_manually(manually),
  better_in_solving_problem(solved_problem_as_application),
  work_with_numbers(no),
  (maths(yes);maths(no)),
  deal_with_deal_with_circuits(no),
  chemistry(yes),
  (physics(yes);physics(no)),
  (biology(yes);biology(no)),
  write('Recommendation: Chemical Engineering '),
  nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Process Engineer'),nl,
  write('- Quality Assurance Engineer'),nl,
  write('- Chemical & Biochemical Engineer'),nl,
  write('- Contamination Engineer').

stream(biotechnology) :-
  btech_or_mtech(btech),
  computer_systems(no),
  computer_or_manually(manually),
  better_in_solving_problem(solved_problem_as_application),
  work_with_numbers(no),
  biology(yes),
  chemistry(yes),
  (maths(yes);maths(no)),
  (physics(yes);physics(no)),
  genetic_engineering(yes),
  write('Recommendation: Biotechnology '),
  nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Pharmaceutical Research & Development'),nl,
  write('- Pharmaceutical Marketing Director'),nl,
  write('- Clinical Trial Manager'),nl,
  write('- Clinical Research Scientist'),nl,
  write('- Biomedical & Biotechnology Research Scientist'),nl,
  write('- Medical & Scientific Product Specialist'),nl,
  write('- Medical Laboratories Director'),nl,
  write('- Academia (Science Educator)').

%Mtech_streams
% Mtech stream finding, it will asks some question to you and give the suitable response according to your answer
% function called for different program such as cse, biotechnology, ece, data engineering, AI engineering.

stream(computer_science) :-
  btech_or_mtech(mtech),
  btech_level_stream(cse),
  computer_systems(yes),
  (technology(apply);technology(develop)),
  (dealing_with_data(yes),dealing_with_data(no)),
  deal_with_circuits(no),
  biology(no),
  write('Recommendation: Computer Science '),nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Software Engineer'),nl,
  write('- System Engineer'),nl,
  write('- Mobile App Developer'),nl,
  write('- Game Developer'),nl,
  write('- System Designer'),nl,
  write('- Network Specialist'),nl,
  write('- Research Analyst'),nl,
  write('- Software Quality Assurance Officer'),nl.

stream(data_engineering) :-
  btech_or_mtech(mtech),
  btech_level_stream(cse),
  computer_systems(yes),
  (technology(apply);technology(develop)),
  dealing_with_data(yes),
  deal_with_circuits(no),
  biology(no),
  write('Recommendation: Data engineering'),nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Software Engineer'),nl,
  write('- Business Intelligence Analysts'),nl,
  write('- Data Architect'),nl,
  write('- Solution Architect'),nl,
  write('- Machine Learning Engineer'),nl,
  write('- Research Analyst'),nl.

stream(aritifical_intelligence) :-
  btech_or_mtech(mtech),
  btech_level_stream(cse),
  computer_systems(yes),
  (technology(apply);technology(develop)),
  (dealing_with_data(yes);dealing_with_data(no)),
  deal_with_circuits(no),
  biology(no),
  write('Recommendation: Aritifical Intelligence'),nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Software Engineer'),nl,
  write('- Business Intelligence Developer'),nl,
  write('- AI Architect'),nl,
  write('- Machine Learning Engineer'),nl,
  write('- Data Scientist'),
  write('- Big Data Engineer'),nl,
  write('- Research Analyst'),nl.

stream(computational_biology) :-
  btech_or_mtech(mtech),
  (btech_level_stream(biotechnology);btech_level_stream(cse)),
  computer_systems(no),
  (technology(apply);technology(develop)),
  (dealing_with_data(yes);dealing_with_data(no)),
  deal_with_circuits(no),
  biology(yes),
  write('Recommendation: Computational Biology '),
  nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Pharmaceutical Research & Development'),nl,
  write('- Pharmaceutical Marketing Director'),nl,
  write('- Clinical Trial Manager'),nl,
  write('- Clinical Research Scientist'),nl,
  write('- Biomedical & Biotechnology Research Scientist'),nl,
  write('- Medical & Scientific Product Specialist'),nl,
  write('- Medical Laboratories Director'),nl,
  write('- Academia (Science Educator)').

stream(electrical_engineering) :-
  btech_or_mtech(mtech),
  btech_level_stream(ece),
  computer_systems(no),
  (technology(apply);technology(develop)),
  (dealing_with_data(yes);dealing_with_data(no)),
  deal_with_circuits(yes),
  biology(no),
  write('Recommendation: Electronics/Electrical Engineering '),
  nl,
  write('After completion of recommended stream you can choose below career path:'),nl,
  write('- Electrical or Electronic Engineer'),nl,
  write('- Technical Director'),nl,
  write('- Network Planning Engineer'),
  write('- Desktop Support Engineer'),nl,
  write('- Electronics Device and Development Engineer').

% knowledge base
% questions_to_user
% asking some question to user to provide the explicit learning to the systems get idea about user knowledge and interest.

ask_to_user(btech_or_mtech) :-
  write('Looking for B.tech level or M.tech level Courses?'),nl.

ask_to_user(btech_level_stream):-
  write('which stream you have taken in your B.tech'),nl.

ask_to_user(dealing_with_data):-
  write('Are you interested in data manipulation and work on data'),nl.

ask_to_user(physics) :-
  write('Do you have interest in Physics?'), nl.

ask_to_user(maths) :-
  write('Do you have interest in Maths?'), nl.

ask_to_user(computer_or_manually) :-
  write('What would you prefer working on a computer or working manually?'), nl.

ask_to_user(work_with_numbers) :-
  write('Do you like dealing with numbers like manipulating it playing around it ?'), nl.

ask_to_user(computer_systems) :-
  write('Are you interested in knowing the details of computer how it work or just happy with using it?'), nl.

ask_to_user(technology) :-
  write('Would you like to develop technology or like to simply apply it?'), nl.

ask_to_user(better_in_solving_problem) :-
  write('Are you better in solving problems?'), nl.

ask_to_user(deal_with_circuits) :-
  write('Are you interested in dealing with circuits and learning more about it?'), nl.

ask_to_user(chemistry) :-
  write('Do you like Chemistry?'), nl.

ask_to_user(biology) :-
  write('Do you like Biology?'), nl.

ask_to_user(genetic_engineering) :-
  write('Are you interested in genetic engineering?'), nl.

% recording  User response later in program I have connected it with the choices which user has selected
user_response(btech) :-
  write('B.tech').

user_response(mtech) :-
  write('M.tech').

user_response(cse):-
  write('Computer Science').

user_response(ece):-
  write('Electrical/Electronic Engineering').

user_response(biotechnology):-
  write('Biotecnology').

user_response(solving_problem) :-
  write('Solving Problem.').

user_response(math) :-
  write('Math.').

user_response(solved_problem_as_application) :-
  write('Using solved problem as application.').

user_response(computer) :-
  write('I would love to work on computer.').

user_response(manually) :-
  write('I prefer working manually.').

user_response(yes) :-
  write('Yes.').

user_response(no) :-
  write('No.').

user_response(apply) :-
  write('I prefer applying technology.').

user_response(develop) :-
  write('I prefer developing technology.').

% Assigning User_response to questions asked by the System

btech_or_mtech(User_response) :-
  progress(btech_or_mtech, User_response).
btech_or_mtech(User_response) :-
  \+ progress(btech_or_mtech, _),
  ask(btech_or_mtech, User_response, [btech, mtech]).

btech_level_stream(User_response) :-
  progress(btech_level_stream, User_response).
btech_level_stream(User_response) :-
  \+ progress(btech_level_stream, _),
  ask(btech_level_stream, User_response, [cse, ece,biotechnology]).

dealing_with_data(User_response) :-
  progress(dealing_with_data, User_response).
dealing_with_data(User_response) :-
  \+ progress(bdealing_with_data, _),
  ask(dealing_with_data, User_response, [yes, no]).

physics(User_response) :-
  progress(physics, User_response).
physics(User_response) :-
  \+ progress(physics, _),
  ask(physics, User_response, [yes, no]).

maths(User_response) :-
  progress(maths, User_response).
maths(User_response) :-
  \+ progress(maths, _),
  ask(maths, User_response, [yes, no]).

chemistry(User_response) :-
  progress(chemistry, User_response).
chemistry(User_response) :-
  \+ progress(chemistry, _),
  ask(chemistry, User_response, [yes, no]).

biology(User_response) :-
  progress(biology, User_response).
biology(User_response) :-
  \+ progress(biology, _),
  ask(biology, User_response, [yes, no]).

better_in_solving_problem(User_response) :-
  progress(better_in_solving_problem, User_response).
better_in_solving_problem(User_response) :-
  \+ progress(better_in_solving_problem, _),
  ask(better_in_solving_problem, User_response, [solving_problem, solved_problem_as_application]).

work_with_numbers(User_response) :-
  progress(work_with_numbers, User_response).
work_with_numbers(User_response) :-
  \+ progress(work_with_numbers, _),
  ask(work_with_numbers, User_response, [yes, no]).

% Computer Science Specialist questions
computer_or_manually(User_response) :-
  progress(computer_or_manually, User_response).
computer_or_manually(User_response) :-
  \+ progress(computer_or_manually, _),
  ask(computer_or_manually, User_response, [computer, manually]).

computer_systems(User_response) :-
  progress(computer_systems, User_response).
computer_systems(User_response) :-
  \+ progress(computer_systems, _),
  ask(computer_systems, User_response, [yes, no]).

technology(User_response) :-
  progress(technology, User_response).
technology(User_response) :-
  \+ progress(technology, _),
  ask(technology, User_response, [apply, develop]).

% electrical or electronic Engineering related questions
deal_with_circuits(User_response) :-
  progress(deal_with_circuits, User_response).
deal_with_circuits(User_response) :-
  \+ progress(deal_with_circuits, _),
  ask(deal_with_circuits, User_response, [yes, no]).

% biotechnology related question
genetic_engineering(User_response) :-
  progress(genetic_engineering, User_response).
genetic_engineering(User_response) :-
  \+ progress(genetic_engineering, _),
  ask(genetic_engineering, User_response, [yes, no]).

% displaying the options for the question asked to user which is stored in list for convenience of user to select correct option

user_responses([], _).
user_responses([First|Rest], Index) :-
  write(Index), write('. '), user_response(First), nl,
  NextIndex is Index + 1,
  user_responses(Rest, NextIndex).

% Parses an Index and returns a user_response at the Indexth element in choice list

parse(0, [First|_], First).
parse(Index, [First|Rest], Response) :-
  Index > 0,
  NextIndex is Index - 1,
  parse(NextIndex, Rest, Response).


% Asks the questions to the user and saves the User_response and based on the response of user returning the stream later on the stream function
% it is taking question, user_responses and choice list match them accordingly and return it.

ask(Ask_to_user, User_response, Choices) :-
  ask_to_user(Ask_to_user),
  user_responses(Choices, 0),
  read(Index),
  parse(Index, Choices, Response),
  asserta(progress(Ask_to_user, Response)),
  Response = User_response.
