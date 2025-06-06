      SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP,
     1                 TEMP,PRESS,SNAME)
C
      INCLUDE 'ABA_PARAM.INC'


      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME

      v=5
      q=1152000.0
      d=v*TIME(2)

      x=COORDS(1)
      y=COORDS(2)
      z=COORDS(3)

      x0=0.0
      y0=2.0
      z0=-4.0
	  
      a=3
      b=3
      c=3
      aa=6
      f1=1.0
      PI=3.1415926
      
      heat1=6.0*sqrt(3.0)*q/(a*b*c*PI*sqrt(PI))*f1
      heat2=6.0*sqrt(3.0)*q/(aa*b*c*PI*sqrt(PI))*(2.0-f1)
	  
      shape1=exp(-3.0*(z-z0-d)**2/a**2-3.0*(y-y0)**2/b**2
     $	-3.0*(x-x0)**2/c**2)
      shape2=exp(-3.0*(z-z0-d)**2/aa**2-3.0*(y-y0)**2/b**2
     $	-3.0*(x-x0)**2/c**2)

C     JLTYP＝1，表示为体热源
      JLTYP=1
	  IF(z .GE.(z0+d)) THEN
	  FLUX(1)=heat1*shape1
	  ELSE
	  FLUX(1)=heat2*shape2
	  ENDIF
      RETURN
      END