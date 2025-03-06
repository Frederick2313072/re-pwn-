// 没有配置文件
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(int argc, char **argv)
{
    lsh_loop(); // 调用循环函数
    return EXIT_SUCCESS;
}
void lsh_loop(void) // 打印一个提示，调用一个函数读取一行，将行拆分为参数，并执行这些函数，释放之前创建的行和参数
{
    char *line;
    char **args;
    int status;
    do
    {
        printf(">");
        line = lsh_read_line();
        args = lsh_split_line(line);
        status = lsh_execute(args);
        free(line);
        free(args);
    } while (status);
}
char *lsh_read_line()
{
    int bufsize = LSH_RL_BUFSIZE;
    int position = 0;
    char *c = buffer = malloc(sizeof(char) * bufsize);
    int c;
    if (!buffer)
    {
        fprintf(stderr, "lsh: allocation error\n"); // 将字符串写入文件stderr
        exit(EXIT_FAILURE);
    }
}
#define LSH_RL_BUFSIZE 1024
while (1)
{
    c = getchar();
    if (c == EOF || c == '\n') // 如果是文件结束符就用null替换并返回，否则将字符添加到现有的字符串中
    {
        buffer[position] = '\0';
        return buffer;
    }
    else
    {
        buffer[position] = c;
    }
    position++;
    if (position >= bufsize)
    {
        bufsize += LSH_RL_BUFSIZE;
        buffer = realloc(buffer, bufsize);
        if (!buffer)
        {
            fprintf(stderr, "lsh: allocation error\n");
            exit(EXIT_FAILURE);
        }
    }
}
#define LSH_TOK_BUFSIZE 64
#define LSH_TOK_DELIM " \t\r\n\a"
char **lsh_split_line(char *line)
{
    int bufsize = LSH_TOK_BUFSIZE, position = 0;
    char **tokens = malloc(bufsize * sizeof(char *));
    char *token;
    if (!tokens)
    {
        fprintf(stderr, "lsh: allocation error\n");
        exit(EXIT_FAILURE);
    }
    token = strtok(NULL, LSH_TOK_DELIM); // 分割字符串
    tokens[position] = NULL;
    return tokens;
}
int lsh_launch(char **arge) // 启动进程
{
    pid_t pid, wpid;
    int status;
    pid = fork(); // 区分父进程与子进程
    if (pid == 0)
    {
        // 子进程
        if (execvp(args[0], args) == -1)
        {
            perror("lsh");
        }
        exit(EXIT_FAILURE);
    }
    else if (pid < 0)
    {
        // 错误处理
        perror("lsh");
    }
    else
    {
        // 父进程
        do
        {
            wpid = waitpid(pid, &status, WUNTRACED);
        } while (!WIFEXITED(status) && !WIFSIGNALED(status));
    }
    return 1;
}
// 内建命令
int lsh_cd(char **args);
int lsh_help(char **args);
int lsh_exit(char **args);
char *builtin_str[] = {
    "cd",
    "help",
    "exit"};
int (*built_func[])(char **) = {
    &lsh_cd,
    &lsh_help,
    &lsh_exit};
int lsh_num_builtins()
{
    return sizeof(builtin_str) / sizeof(char *);
}
int lsh_cd(char **args)
{
    if (args[1] == NULL)
    {
        fprintd(stderr, "lsh: expected argument to \"cd\"\n");
    }
    else
    {
        if (chdir(args[0] != 0))
        {
            perror("lsh");
        }
    }
    return 1;
}
int lsh_help(char **args)
{
    int i;
    printf("Liu Shihao's LSH\n");
    printf("Type program names and arguments, and hit enter.\n");
    printf("The following are built in:\n");
    for (i = 0; i < lsh_num_builtins(); i++)
    {
        printf(" %s\n", builtin_str[i]);
    }
    printf("Use the man command for information on other programs.\n");
    return 1;
}
int lsh_exit(char **args)
{
    return 0;
}
int lsh_execute(char **args)
{
    int i;

    if (args[0] == NULL)
    {
        // An empty command was entered.
        return 1;
    }

    for (i = 0; i < lsh_num_builtins(); i++)
    {
        if (strcmp(args[0], builtin_str[i]) == 0)
        {
            return (*builtin_func[i])(args);
        }
    }

    return lsh_launch(args);
}
