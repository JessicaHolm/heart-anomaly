# Heart Anomaly

Jason Holm

This is a machine learner that uses Naïve Bayesian learning to classify hearts as normal or anomalous.

Run with `python3 heart.py [training_file] [test_file]`.

Example result: `orig 142/187 (0.76) 10/15 (0.67) 132/172 (0.77)`.

The first number is the percentage of instances that were classified correctly.
The second number is the percentage of anomalus instances that were classified correctly.
The third number is the percentage of normal instances that were classified correctly.

My testing was done on Windows Subsystem for Linux (WSL) under Ubuntu using a Intel i5-4460 CPU @ 3.20GHz.
