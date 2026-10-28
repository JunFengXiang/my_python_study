# 附录 D 使用 Git 进行版本控制

> 本附录已由 AI 逐页对照原页转写，尚未经人工复核。命令和示例输出保留原书，未执行会修改环境的操作。

[返回目录](README.md) | PDF 原页 698–714

## PDF 第 698 页

<!-- page-status: reviewed -->

[查看原 PDF 第 698 页](images/page-0698.jpg)

# 附录 D 使用 Git 进行版本控制

版本控制软件让你能够为处于可行状态的项目创建快照。修改项目（如实现新功能）后，如果项目不能正常运行，可恢复到上一个可行状态。

使用版本控制软件，你可以放手大胆地改进项目，不用担心项目因你犯错而遭到破坏。这不仅对于大型项目来说尤其重要，对于较小的项目（哪怕是只包含一个文件的程序）来说也大有裨益。

在本附录中，你将学习如何安装 Git，以及如何使用它来对当前开发的程序进行版本控制。Git 是当前最流行的版本控制软件，它不仅包含很多高级工具，可帮助团队协作开发大型项目，而且其最基本的功能也非常适合独立的开发人员使用。Git 通过跟踪对项目中每个文件的修改来实现版本控制。如果你犯了错，只需恢复到保存的上一个状态即可。

## PDF 第 699 页

<!-- page-status: reviewed -->

[查看原 PDF 第 699 页](images/page-0699.jpg)

### D.1 安装 Git

Git 可在所有操作系统上运行，但安装方法随操作系统而异。接下来的几小节详细说明了如何在各种操作系统中安装它。

有些系统默认安装了 Git，通常是随你安装的其他包一起安装的。在尝试安装 Git 前，看看系统是否已安装了它：打开一个终端窗口，并执行命令 `git --version`。如果在输出中看到了具体的版本号，就说明系统安装了 Git。如果看到一条消息，提示你安装或升级 Git，只需按屏幕上的说明做即可。

如果在屏幕上没有看到任何说明且你使用的是 Windows 或 macOS，可从 Git 的官方网站上下载安装程序。如果你使用的是与 apt 兼容的 Linux 系统，可使用命令 `sudo apt install git` 来安装 Git。

#### 配置 Git

Git 会跟踪是谁修改了项目，哪怕参与项目开发的人只有一个。为此，Git 需要知道你的用户名和电子邮箱地址。你必须提供用户名，但可使用虚构的电子邮箱地址：

```bash
git config --global user.name "username"
git config --global user.email "username@example.com"
```

如果忘记了这一步，Git 将在你首次提交时提示你提供这些信息。

另外，最好设置每个项目中主分支的默认名称，一个不错的主分支名称是 `main`：

```bash
git config --global init.defaultBranch main
```

上述配置意味着，在你使用 Git 管理的每个新项目中，一开始都只有一个分支，该分支名为 `main`。

## PDF 第 700 页

<!-- page-status: reviewed -->

[查看原 PDF 第 700 页](images/page-0700.jpg)

### D.2 创建项目

我们来创建一个要进行版本控制的项目。在系统中创建一个文件夹，并将其命名为 `git_practice`。在这个文件夹中，创建一个简单的 Python 程序：

`hello_git.py`

```python
print("Hello Git world!")
```

我们将使用这个程序来探索 Git 的基本功能。

## PDF 第 701 页

<!-- page-status: reviewed -->

[查看原 PDF 第 701 页](images/page-0701.jpg)

### D.3 忽略文件

扩展名为 `.pyc` 的文件是根据 `.py` 文件自动生成的，因此无须让 Git 跟踪它们。这些文件存储在目录 `__pycache__` 中。为了让 Git 忽略这个目录，创建一个名为 `.gitignore` 的特殊文件（这个文件名以句点打头，且没有扩展名），并在其中添加如下一行内容：

`.gitignore`

```gitignore
__pycache__/
```

这会让 Git 忽略目录 `__pycache__` 中的所有文件。使用文件 `.gitignore` 可避免混乱，让项目开发起来更容易。

你可能需要修改文件浏览器的设置，使其显示隐藏的文件（名称以句点打头的文件）：在 Windows 资源管理器中，选择菜单“查看”中的复选框“隐藏的项目”；在 macOS 系统中，按组合键 Command + Shift + .（句点）；在 Linux 系统中，查找并选择设置 Show Hidden Files（显示隐藏的文件）。

> **注意：**如果你使用的是 macOS 系统，请在文件 `.gitignore` 中再添加一行：`.DS_Store`。因为在 macOS 系统中，每个目录都有隐藏的文件 `.DS_Store`，其中包含有关当前目录的信息。如果不将它们加入 `.gitignore`，项目将混乱不堪。

## PDF 第 702 页

<!-- page-status: reviewed -->

[查看原 PDF 第 702 页](images/page-0702.jpg)

### D.4 初始化仓库

前面创建了一个目录，其中包含一个 Python 文件和一个 `.gitignore` 文件，现在可以初始化一个 Git 仓库了。为此，打开一个终端窗口，切换到文件夹 `git_practice`，并执行如下命令：

```bash
git init
```

```text
git_practice$ git init
Initialized empty Git repository in git_practice/.git/
git_practice$
```

输出表明 Git 在 `git_practice` 中初始化了一个空仓库。**仓库**（repository）是程序中被 Git 主动跟踪的一组文件。Git 用来管理仓库的文件都存储在隐藏的目录 `.git` 中。虽然你根本不需要与这个目录打交道，但千万不要删除它，否则将丢失项目的所有历史记录。

## PDF 第 703 页

<!-- page-status: reviewed -->

[查看原 PDF 第 703 页](images/page-0703.jpg)

### D.5 检查状态

执行其他操作前，看一下项目的状态：

```bash
git status
```

```text
  git_practice$ git status
❶ On branch main
  No commits yet

❷ Untracked files:
    (use "git add <file>..." to include in what will be committed)
        .gitignore
        hello_git.py

❸ nothing added to commit but untracked files present (use "git add" to
track)
  git_practice$
```

在 Git 中，**分支**（branch）是项目的一个版本。从这里的输出可知，我们位于分支 `main` 上（见 ❶）。每当查看项目的状态时，输出都将指出位于分支 `main` 上。接下来的输出表明，还未执行任何提交。**提交**（commit）是项目在特定时间点的快照。

Git 指出了项目中未被跟踪的文件（见 ❷），因为还没有告诉它要跟踪哪些文件。接下来，Git 告诉我们没有将任何东西添加到当前的提交中，并且指出了可能需要加入仓库的未跟踪文件（见 ❸）。

## PDF 第 704 页

<!-- page-status: reviewed -->

[查看原 PDF 第 704 页](images/page-0704.jpg)

### D.6 将文件加入仓库

下面将这两个文件加入仓库，并再次检查状态：

```text
❶ git_practice$ git add .
❷ git_practice$ git status
  On branch main
  No commits yet

  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
❸       new file:   .gitignore
        new file:   hello_git.py

  git_practice$
```

命令 `git add .` 将项目中未被跟踪的所有文件（条件是没有在 `.gitignore` 中列出）都加入仓库（见❶）。它不提交这些文件，只是让 Git 关注它们。现在检查项目的状态，会发现 Git 找出了一些需要提交的修改（见❷）。`new file` 意味着这些文件是新添加到仓库中的（见❸）。

> 校对注：`git add .` 还会暂存当前目录及其子目录中已跟踪文件的修改和删除，并非只处理新文件；它是放入暂存区，尚未创建提交。运行前可用 `git status` 检查范围。

## PDF 第 705 页

<!-- page-status: reviewed -->

[查看原 PDF 第 705 页](images/page-0705.jpg)

### D.7 执行提交

下面来执行第一次提交：

```text
❶ git_practice$ git commit -m "Started project."
❷ [main (root-commit) cea13dd] Started project.
❸ 2 files changed, 5 insertions(+)
   create mode 100644 .gitignore
   create mode 100644 hello_git.py
❹ git_practice$ git status
  On branch main
  nothing to commit, working tree clean
  git_practice$
```

我们执行命令 `git commit -m "message"`（见❶）创建项目的快照。标志 `-m` 让 Git 将接下来的消息（`Started project.`）记录到项目的历史记录中。输出表明我们位于分支 `main` 上（见❷）且有两个文件被修改了（见❸）。

现在检查状态，将发现我们位于分支 `main` 上且工作树是干净的（见❹）。这是在每次提交项目的可行状态时都应该看到的消息。如果显示的消息不是这样的，请仔细阅读，很可能是你在提交前忘记了添加文件。

## PDF 第 706 页

<!-- page-status: reviewed -->

[查看原 PDF 第 706 页](images/page-0706.jpg)

### D.8 查看提交历史

Git 记录所有的项目提交。下面来看一下提交历史：

```text
git_practice$ git log
commit cea13ddc51b885d05a410201a54faf20e0d2e246 (HEAD -> main)
Author: eric <eric@example.com>
Date:   Mon Jun 6 19:37:26 2022 -0800

    Started project.
git_practice$
```

每次提交时，Git 都会生成一个独一无二的引用 ID，长度为 40 个字符。它记录提交是谁执行的，提交的时间，以及提交时指定的消息。并非在任何情况下都需要所有这些信息，因此 Git 提供了一个选项，让你能够打印提交历史条目的简单版本：

```text
git_practice$ git log --pretty=oneline
cea13ddc51b885d05a410201a54faf20e0d2e246 (HEAD -> main) Started project.
git_practice$
```

标志 `--pretty=oneline` 指定显示两项最重要的信息：提交的引用 ID，以及为提交记录的消息。

## PDF 第 707 页

<!-- page-status: reviewed -->

[查看原 PDF 第 707 页](images/page-0707.jpg)

### D.9 第二次提交

为了展示版本控制的强大威力，我们需要修改项目并提交所做的修改。在 `hello_git.py` 中再添加一行代码：

`hello_git.py`

```python
print("Hello Git world!")
print("Hello everyone.")
```

如果现在查看项目的状态，将发现 Git 注意到这个文件发生了变化：

```text
  git_practice$ git status
❶ On branch main
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working
  directory)

❷ modified:   hello_git.py

❸ no changes added to commit (use "git add" and/or "git commit -a")
  git_practice$
```

输出指出了当前所在的分支（见❶）和被修改了的文件的名称（见❷），还指出了所做的修改未提交（见❸）。下面来提交所做的修改，并再次查看状态：

```text
❶ git_practice$ git commit -am "Extended greeting."
  [main 945fa13] Extended greeting.
   1 file changed, 1 insertion(+), 1 deletion(-)
❷ git_practice$ git status
  On branch main
  nothing to commit, working tree clean
❸ git_practice$ git log --pretty=oneline
  945fa13af128a266d0114eebb7a3276f7d58ecd2 (HEAD -> main) Extended
  greeting.
  cea13ddc51b885d05a410201a54faf20e0d2e246 Started project.
  git_practice$
```

## PDF 第 708 页

<!-- page-status: reviewed -->

[查看原 PDF 第 708 页](images/page-0708.jpg)

我们再次执行提交，并在执行命令 `git commit` 时指定了标志 `-am`（见❶）。标志 `-a` 让 Git 将仓库中所有修改了的文件都加入当前提交。（如果在两次提交之间创建了新文件，可再次执行命令 `git add .` 来将这些新文件加入仓库。）标志 `-m` 让 Git 在提交历史中记录一条消息。

在查看项目的状态时，可以看到工作树是干净的（见❷）。最后，我们发现提交历史中包含两个提交（见❸）。

## PDF 第 709 页

<!-- page-status: reviewed -->

[查看原 PDF 第 709 页](images/page-0709.jpg)

### D.10 放弃修改

下面来看看如何放弃所做的修改，恢复到上一个可行状态。首先在 `hello_git.py` 中再添加一行代码：

`hello_git.py`

```python
print("Hello Git world!")
print("Hello everyone.")

print("Oh no, I broke the project!")
```

保存并运行这个文件。

查看状态，会发现 Git 注意到了所做的修改：

```text
  git_practice$ git status
  On branch main
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working
  directory)

❶     modified:   hello_git.py

  no changes added to commit (use "git add" and/or "git commit -a")
  git_practice$
```

Git 注意到我们修改了 `hello_git.py`（见❶）。如果愿意，可以提交所做的修改，但这次我们不提交所做的修改，而是恢复到最后一个提交（我们知道，那次提交时项目能够正常地运行）。为此，我们不对 `hello_git.py` 执行任何操作（既不删除刚添加的代码行，也不使用文本编辑器的撤销功能），而是在终端会话中执行如下命令：

```text
git_practice$ git restore .
git_practice$ git status
On branch main
nothing to commit, working tree clean
git_practice$
```

## PDF 第 710 页

<!-- page-status: reviewed -->

[查看原 PDF 第 710 页](images/page-0710.jpg)

命令 `git restore filename` 让你能够放弃最后一次提交后对指定文件所做的所有修改。命令 `git restore .` 则放弃最后一次提交后对所有文件所做的所有修改，从而将项目恢复到最后一次提交的状态。

如果此时返回文本编辑器，将发现 `hello_git.py` 被修改成了下面这样：

```python
print("Hello Git world!")
print("Hello everyone.")
```

在这个简单的项目中，恢复到之前某个状态的能力看似微不足道，但如果开发的是大型项目，其中数十个文件都被修改了，那么通过恢复到上一个状态，将撤销最后一次提交后对这些文件所做的所有修改。这个功能很有用：在实现新功能时，可根据需要做任意数量的修改；如果这些修改不可行，可撤销它们，而不会影响项目。你无须记住做了哪些修改并手动撤销所做的修改，Git 会替你完成所有这些工作。

**注意**：要看到已恢复的版本，可能需要在编辑器中刷新文件。

> 校对注：`git restore` 默认恢复工作区中已跟踪文件的更改，不会自动撤销已经暂存的更改，也不会删除未跟踪文件；原文的“所有修改”应结合这些范围理解。

## PDF 第 711 页

<!-- page-status: reviewed -->

[查看原 PDF 第 711 页](images/page-0711.jpg)

### D.11 检出以前的提交

要检出提交历史中的任何提交，可使用命令 `checkout`，并指定该提交的引用 ID 的前 6 个字符。检出并检查以前的提交后，既可以返回最后一次提交，也可以放弃最近所做的工作并选择以前的提交：

```text
git_practice$ git log --pretty=oneline
945fa13af128a266d0114eebb7a3276f7d58ecd2 (HEAD -> main) Extended greeting.
cea13ddc51b885d05a410201a54faf20e0d2e246 Started project.
git_practice$ git checkout cea13d
Note: switching to 'cea13d'.

❶ You are in 'detached HEAD' state. You can look around, make experimental
  changes and commit them, and you can discard any commits you make in this
  state without impacting any branches by switching back to a branch.

  If you want to create a new branch to retain commits you create, you may
  do so (now or later) by using -c with the switch command. Example:

    git switch -c <new-branch-name>

❷ Or undo this operation with:

    git switch -

  Turn off this advice by setting config variable advice.detachedHead to false

  HEAD is now at cea13d Started project.
  git_practice$
```

检出以前的提交后，将离开分支 `main`，并进入 Git 所说的**分离头指针**（detached HEAD）状态（见❶）。`HEAD` 表示当前提交的项目状态。之所以说处于分离状态（detached），是因为离开了一个具名分支（这里是 `main`）。

要回到分支 `main`，可按建议（见❷）所说的那样撤销上一个操作：

## PDF 第 712 页

<!-- page-status: reviewed -->

[查看原 PDF 第 712 页](images/page-0712.jpg)

```text
git_practice$ git switch -
Previous HEAD position was cea13d Started project.
Switched to branch 'main'
git_practice$
```

这样就回到分支 `main` 了。除非要使用 Git 的高级功能，否则在检出以前的提交后，最好不要对项目做任何修改。然而，如果参与项目开发的人只有你自己，而你又想放弃最近的所有提交并恢复到以前的状态，也可将项目重置到以前的提交。为此，可在处于分支 `main` 上的情况下，执行如下命令：

```text
❶ git_practice$ git status
  On branch main
  nothing to commit, working directory clean
❷ git_practice$ git log --pretty=oneline
  945fa13af128a266d0114eebb7a3276f7d58ecd2 (HEAD -> main) Extended greeting.
  cea13ddc51b885d05a410201a54faf20e0d2e246 Started project.
❸ git_practice$ git reset --hard cea13d
  HEAD is now at cea13dd Started project.
❹ git_practice$ git status
  On branch main
  nothing to commit, working directory clean
❺ git_practice$ git log --pretty=oneline
  cea13ddc51b885d05a410201a54faf20e0d2e246 (HEAD -> main) Started project.
  git_practice$
```

首先查看状态，确认位于分支 `main` 上（见❶）。在查看提交历史时，我们看到了两个提交（见❷）。接下来，执行命令 `git reset --hard`，并在其中指定要永久恢复到的提交的引用 ID 的前 6 个字符（见❸）。再次查看状态，可以发现位于分支 `main` 上且没有需要提交的修改（见❹）。再次查看提交历史，将发现我们回到了要从它重新开始的提交（见❺）。

> 校对注：`git reset --hard` 会重置分支和已跟踪文件的暂存区、工作区，可能丢失未保存修改；此处是书中的示例输出，不应对正在使用的仓库直接照搬。

## PDF 第 713 页

<!-- page-status: reviewed -->

[查看原 PDF 第 713 页](images/page-0713.jpg)

### D.12 删除仓库

有时候，仓库的历史记录被弄乱了，而你又不知道如何恢复。在这种情况下，首先应考虑使用附录 C 介绍的方法寻求帮助。如果无法恢复且参与项目开发的只有你一个人，可继续使用这些文件，但将项目的历史记录删除——删除目录 `.git`。这不会影响任何文件的当前状态，只会删除所有的提交，因此将无法检出项目的其他任何状态。

为此，既可以打开一个文件浏览器并将目录 `.git` 删除，也可以通过命令行将其删除。之后，需要重新创建一个仓库，以便重新对修改进行跟踪。下面演示了如何在终端会话中完成这个过程：

```text
❶ git_practice$ git status
  On branch main
  nothing to commit, working directory clean
❷ git_practice$ rm -rf .git/
❸ git_practice$ git status
  fatal: Not a git repository (or any of the parent directories): .git
❹ git_practice$ git init
  Initialized empty Git repository in git_practice/.git/
❺ git_practice$ git status
  On branch main
  No commits yet

  Untracked files:
    (use "git add <file>..." to include in what will be committed)
        .gitignore
        hello_git.py

  nothing added to commit but untracked files present (use "git add" to track)
❻ git_practice$ git add .
  git_practice$ git commit -m "Starting over."
  [main (root-commit) 14ed9db] Starting over.
   2 files changed, 5 insertions(+)
   create mode 100644 .gitignore
   create mode 100644 hello_git.py
❼ git_practice$ git status
  On branch main
  nothing to commit, working tree clean
  git_practice$
```

> 校对注：删除 `.git` 会移除本地仓库的提交历史、配置和其他 Git 元数据；这是破坏性操作，请不要在需要保留历史的仓库执行。

## PDF 第 714 页

<!-- page-status: reviewed -->

[查看原 PDF 第 714 页](images/page-0714.jpg)

首先查看状态，发现工作树是干净的（见❶）。接下来，使用命令 `rm -rf .git/`（在 Windows 系统中为 `del .git`）删除目录 `.git`（见❷）。删除文件夹 `.git` 后再次查看状态，将被告知这不是一个 Git 仓库（见❸）。Git 用来跟踪仓库的信息都存储在文件夹 `.git` 中，因此删除该文件夹意味着删除整个仓库。

接下来，使用命令 `git init` 新建一个全新的仓库（见❹）。然后查看状态，发现又回到了初始状态，等待着第一次提交（见❺）。我们将所有文件都加入仓库，并执行第一次提交（见❻）。之后再次查看状态，会发现我们位于分支 `main` 上且没有任何未提交的修改（见❼）。

你需要一些练习才能学会使用版本控制，但一旦开始使用，你就再也离不开它了。

> 校对注：`del .git` 是原书写法；在 Windows 命令提示符中 `del` 用于删除文件，不能作为删除 `.git` 目录的通用命令。删除 Git 元数据有破坏性，请先确认目标和备份。

