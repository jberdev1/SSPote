#include <iostream>
#include <windows.h>
using namespace std;

LRESULT WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam){
  if (WM_POWERBROADCAST == message && PBT_APMSUSPEND == wParam){
      system("py C:/Users/jtria/OneDrive/Documents/SSPote/SSPote.py test");
  }
  return DefWindowProc(hWnd, message, wParam, lParam);
}

int main()
{
    cout << "Hello world!" << endl;
    while(1);
    return 0;
}
