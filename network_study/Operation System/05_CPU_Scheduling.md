# CPU Scheduling

 CPU and I/O Bursts in Program Execution, CPU-burst Time의 분포, CPU Scheduler & Dispatcher, Scheduling Algorithms, Scheduling Criteria, FCFS(First- Come First-Served), SJF(Shortest-Job-First), Example of Non-Preemptive SJF, Example of Preemptive SJF, 다음 CPU Burst Time의 예측, Exponential Averaging, Priority Scheduling, Round Robin(RR), Example: RR with Time Quantum = 20, Turmaround Time Varies With Time Quantum

 CPU-burst Time의 분포, Schedulling Algorithms, Round Robin(RR), Multilevel Queue, Multilevel Feedback Queue, Multi-Processor Scheduling, Real-time Scheduling, Example of Non-Preemptive SJF, Thread Scheduling, Algorithm Evaluation, 39:12





CPU and I/P Bursts in Program Execution



* 여러 종류의 프로세스가 섞여 있어서 어떤 프로세스에 cpu를 줄지 결정하는 스케쥴링이 필요함
  * 문제점 2가지
    * 누구한테 당장 cpu를 줄 것인지
    * 너무 오래 사용할 경우, 뺏어서 누구에게 줄 것인지를 결정해야 함
* 스케쥴링 성능을 측정하는 성능 척도
  * 시스템 입장
    * 이용률
    * 처치량
  * 프로그램 입장
    * 소요시간
    * 대기시간
    * 응답시간
  * 효율적으로 사용하기 위해 스케쥴링 알고리즘이 존재
    * FCFS (First-Come First-Served)
      * 먼저 온 순서대로 처리
    * SJF (Shortest-Job-First)
      * 짧게 쓰는 것들을 먼저 처리하는 것
    * Priority Scheduling (우선순위 스케쥴링)
    * Round Robin(RR)
      * 각 프로세스는 동일한 크기의 할당 시간을 가짐
      * 할당 시간이 지나면 뺏기고 ready queue의 뒤에 서게 됨
      * 장점: 응답 시간이 빨라짐
    * Multilevel Queue
      * 우선순위 순서대로 줄을 섬 (계급처럼 정해져 있음)



* **Multiple-Processor Scheduling(CPU가 여러개인 경우의 알고리즘)**

  * Hmogeneous processor

  * Load sharing

  * Symm Multiprocessing

  * Asymm Multiprocessing