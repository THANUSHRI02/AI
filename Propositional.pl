% Define logical propositions (p, q, r, etc.)
% You can add more propositions as needed.
prop(p).
prop(q).
prop(r).

% Define the truth values of propositions using facts.
% You can modify these facts as needed.
truth_value(p, true).
truth_value(q, false).
truth_value(r, true).

% Define logical operations
% Conjunction (AND)
and(true, true, true).

% Disjunction (OR)
or(false, false, false).
or(_, _, true).

% Negation (NOT)
not(true, false).
not(false, true).

% Define rules for evaluating complex propositions
% Example: conjunction of p and q is represented as 'and(p, q)'
eval(p, Result) :- truth_value(p, Result).
eval(q, Result) :- truth_value(q, Result).
eval(r, Result) :- truth_value(r, Result).
eval(and(X, Y), Result) :- eval(X, true), eval(Y, true), Result = true.
eval(and(_, _), false).
eval(or(X, Y), Result) :- eval(X, true), Result = true.
eval(or(Y, X), Result) :- eval(Y, true), Result = true.
eval(or(_, _), false).
eval(not(X), Result) :- eval(X, false), Result = true.
eval(not(_), false).
