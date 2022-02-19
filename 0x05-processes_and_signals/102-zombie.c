#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 * Return: value 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_zombie - creates 5 zombie processes
 * Return: pid of process zombie
 */
pid_t create_zombie()
{
	pid_t zombie;
	zombie = fork();
	return zombie;
}

/**
 * main - start program execution
 * Return: value 0
 */
int main(void)
{
	int i = 0;

	while (i < 5)
	{
		pid_t zombie = create_zombie();
		if (!zombie)
			return(0);
		printf("Zombie process created, PID: %d\n", zombie);
		i++;
	}
	infinite_while();
	return (0);
}
