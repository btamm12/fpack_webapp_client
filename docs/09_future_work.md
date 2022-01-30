[\[Back\]](./README.md) \
🔲🔲🔲🔲🔲🔲🔲🔲⏹ \
[\[<---\]](./08_sending_your_results.md) \[--->\]

# 9. Future Work (Developers)

**This section is aimed towards the developers. It contains aspects of the project
that can still be improved.**

## 9.1. Proper Web Service

### 9.1.1. Security Concerns

For security reasons, my ESAT web server
```
https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v0/
```
only allows client-side code execution, i.e. displaying web pages, downloading files
and running JavaScript on the client side.

It is possible to enable PHP (server-side language) on my ESAT homes webpage by
creating a ticket with [ESAT
IT](https://securewww.esat.kuleuven.be/helpdesk/logcall.php?DBname=itcalls) (this is
an ESAT internal link).

**But to do it properly would take about two weeks of work according to the ESAT IT
expert Bert Deknuydt:**
- Triggering a Condor job from PHP, careful with secuity (1 week)
- Returning results after Condor job is finished, polling is last resort (1 week)

Another point Bert made was about storing sensitive data in my public_html/ folder
(where the web pages are stored):
> Dumping in public_html, ok, why not, but it seems security is extra important here
> as it's medical stuff.  You'd have to work with random-number-subdirectories, so
> that it cannot be 'found' by anyone else than the submitter.

Finally, there is the danger of annotators messing with data that is not theirs.
> So you need a system with accounts and a kind of file-results-repo, accessible only
> by the submitter. Feasible for sure, but not easy. 

This is something I implemented with the "subject mapping" file. Thus, only someone
with the "subject mapping" file can locate a participant's data, even if he already
knows that `sXXX` is the pseudonym for the desired participant "John Doe".

### 9.1.2. Annotator Registration Process

Currently, the annotators need to cooperate to ensure they are not annotating the
same files, which would be a waste of time.

In a later version of the tool, the annotators could register for an account in the
web server.

When an admin grants the annotator access (by creating the account), they will be
automatically sent the "subject mapping" file, which can be different for different
users.

### 9.1.3. Cooperation Between Annotators

Then they can select which sections they would like to annotate from the server. The
server knows which users have selected which sections, so it can prevent a section
from being selected twice.

### 9.1.4. Submitting Condor Requests

Currently, some intervention is needed by someone with ESAT account in order to
create the CTM files.

In a later version of the tool, it may be possible to have the annotators submit the
Condor requests themselves through the web service. This would make the process
completely automated.

**Condor Concerns:**

Condor can be tricky. Submitting a valid Condor job file does not always mean your
job will run: sometimes a machine will "have a brainfart" and not be able to execute
a simple script.

In order to trust that the Condor jobs will run, a Condor-job managing system would
need to be implemented. This system would detect if a job
1. ran successfully;
2. is taking too long because of an extremely slow compute node;
3. crashed due to a programming error; or
4. crashed due to a machine error.

When an anomaly is detected (case 2,3,4), the managing system should stop the job,
exclude the bad machine, and resubmit the job.

I have already implemented such a system for another project. Unless someone can
think of a simpler way of avoiding this problem?
