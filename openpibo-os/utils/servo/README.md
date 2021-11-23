## note
 + 20210209
  - Delete total, speed/acceleration all command
  - update

## Installation
sudo ./install.sh

## Check
 - baudrate : 9600, 19200, 38400, 57600, 115200(default)

## Command
 + Comand List
  - servo move POS0<-900~900> POS1<-900~900> ... POS9<-900~900> TIME<ms>
  - servo mwrite POS0<-900~900> POS1<-900~900> ... POS9<-900~900>
  - servo write MOTOR<0~9> POS<-900~900>
  - servo twrite SPEED<0~255> ACCELERATION<0~255> MOTOR<0~9>
  - servo speed (all | MOTOR<0~9>) SPEED<0~255>
  - servo accelerate (all | MOTOR<0~9>) ACCELERATION<0~255>
  - servo help
  - servo version
  - servo init
  - servo profile init
  - servo profile offset get
  - servo profile offset set POS0<-900~900> POS1<-900~900> ... POS9<-900~900>
  - servo profile pos get
  - servo profile pos set POS0<-900~900> POS1<-900~900> ... POS9<-900~900>
  - servo profile record get

 + For Example:
  - servo write 0 0
