ó
Ç¯Uc           @   sL   d  d l  Z d  d l j Z d   Z d   Z d   Z d   Z d   Z	 d S(   iÿÿÿÿNc         C   sË  t  d |  d  } | j d  d } d } xzt |  D]l} xct | |  D]R} | | d k  ró t  d |  | | f d  } t  d	 |  | f d  } | j   d
 }	 |	 j   d }
 | j   d
 j   d } |
 | k r¡| j |	  q¡qO | | d k rO | } | d } t  d |  | | f d  } t  d	 |  | f d  } | j   d
 }	 |	 j   d }
 | j   d
 j   d } |
 | k r¡| j |	  q¡qO qO Wq9 W| j   | j   | j   d  S(   Ns   %s/Interactions30.txtt   ws   Time a e i AoP LoAN MA Mass
i    iÈ   i   s   %s/RunP%r/PM%r.aeit   rs   %s/RunP%r/INNER.aeiiÿÿÿÿ(   t   opent   writet   ranget	   readlinest   splitt   close(   t   run_directoryt   rangeat   st   startt   finisht   nt   zt   fR   t   Plastt   Ptimet   Baselast(    (    s   Survivor.pyt   interactions   s6    


c         C   sy   t  d |  d  } | j d  x> t |  D]0 } t  d |  | f d  } | j   } | GHq- W| j   | j   d  S(   Ns   %s/InteractionTimes20.txtR    t   Times   %s/RunP%r/info.outR   (   R   R   R   R   R   (   R   R	   R
   R   R   t	   All_lines(    (    s   Survivor.pyt   interactions_precise!   s    
c         C   sÖ   t  j |  d d d d } d | } t j   } | j d  } d } | j | d | d	 d
 d t d t d d d d d t | j d  | j	 d  | j
 d  | j d  t j |  t j   t j   d  S(   Nt   skiprowsi   t   usecolsi    s   %s/PlanestesimalInt30Hist.jpegio   i2   t   binst   histtypet   stept   stackedt   fillt   colort   indigot   alphagé?t   normeds0   $Histogram\,of\,Planetesimal\,Interaction\,Time$s   $Time\,(Years)$t   logt   linear(   i    (   t   npt   loadtxtt   pltt   figuret   add_subplott   histt   Falset   Truet	   set_titlet
   set_xlabelt
   set_yscalet
   set_xscalet   savefigt   showR   (   t   fileR   R   t   Histdestt   figt   axesR   (    (    s   Survivor.pyt   interaction_hist1   s    
7
c         C   sË  t  d |  d  } | j d  d } d } xzt |  D]l} xct | |  D]R} | | d k  ró t  d |  | | f d  } t  d	 |  | f d  } | j   d
 }	 |	 j   d }
 | j   d
 j   d } |
 | k r¡| j |	  q¡qO | | d k rO | } | d } t  d |  | | f d  } t  d	 |  | f d  } | j   d
 }	 |	 j   d }
 | j   d
 j   d } |
 | k r¡| j |	  q¡qO qO Wq9 W| j   | j   | j   d  S(   Ns   %s/Survivors30.txtR    s   Time a e i AoP LoAN MA Mass
i    iÈ   i   s   %s/RunP%r/PM%r.aeiR   s   %s/RunP%r/INNER.aeiiÿÿÿÿ(   R   R   R   R   R   R   (   R   R	   R
   R   R   R   R   R   R   R   R   R   (    (    s   Survivor.pyt   survivor_makerF   s6    


c         C   s$  g  } t  j |  d d d d. } d | } d } d } xê t |  D]Ü } xÓ t | |  D]Â }	 |	 | d k  r¶ t d | | |	 f d  }
 | j t |
 j   d	 j   d   qZ |	 | d k rZ | } | d } t d | | |	 f d  }
 | j t |
 j   d	 j   d   qZ qZ WqD W|
 j   t	 j
   } | j d
  } d } | j | d | d d d g d d d t d t d d d d d d | j | d | d d d g d d d t d t d d d d d d d d d d 
| j d  d d g } d  d  g } d! d! g } d d" g } t	 j | |  } t	 j | |  } t	 j | |  } t	 j | d d d# d$ t	 j | d d% d# d$ t	 j | d d& d# d$ | j d'  | j d(  | j d)  | j d)  | j d* d+ g  | j d d" g  | j d, d-  t	 j |  t	 j   d  S(/   NR   i   R   s   %s/PlanestesimalSep30Hist.jpegi    iÈ   s   %s/RunP%r/PM%r.aeiR   i   io   iú   R   R   g{®Gáz?R   R   R   R   R   t   tealt   labelt   InitialR!   R+   R   t	   facecolorR    g333333Ó?t   Finals"   Histogram of Planetesimal Distanceg¹?gPäIÒ5Ã?g§yÇ):Ã?i7   t	   linewidthg      ð?t   greent   blacks,   $Planetesimal\,Seperation\,after\,30\,Years$s   $Distance\,(AU)$R"   g/Ý$¥?g{®GázÔ?t   loct   best(   i   (   R$   R%   R   R   t   appendt   floatR   R   R   R&   R'   R(   R)   R*   R+   R,   t   plott   setpR-   R.   R/   t   set_xlimt   set_ylimt   legendR0   (   R2   R   R	   t   OrbitalSepinitialt   OrbitalSepfinR3   R   R   R   R   R   R4   R5   R   t   x1t   x2t   x3t   yt   line1t   line2t   line3(    (    s   Survivor.pyt   survivor_histogramg   sR    
*
2
CO(
   t   numpyR$   t   matplotlib.pyplott   pyplotR&   R   R   R6   R7   RR   (    (    (    s   Survivor.pyt   <module>   s   				!