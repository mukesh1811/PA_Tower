#include <iostream>

void callTry()
{
  std::cout << "Called successfully";
}

void draw()
{
  int limit_i = 38;
  int limit_j = 100;

  for(int i =0;i<=limit_i;i++)
  {
    for (int j=0;j<=limit_j;j++)
    {
      if(j == 0 || j == limit_j)
      {
        std::cout << "|";
      }

      else if(i == 0 || i == limit_i)
      {
        std::cout << "-";
      }

      else
      {
        std::cout << " ";
      }
    }

    std::cout << "\n";
  }


}

int main()
{
  bool play = true;

  //char quit = 'y';

  //while(play)
 //{

    //if (play)

    //callTry();
    draw();

    //std::cin >> quit;
    ////if(quit == 'q')
    //{
      //play=false;
    //}
  //}
}