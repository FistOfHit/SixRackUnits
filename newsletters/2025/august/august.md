[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# August 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/title.jpeg)

*Is a material form a requirement for true intelligence? Does being limited to certain modalities of input result in less capability within those modalities than an intelligence that can handle more modalities of input? If so, will achieving human-level intelligence require AI models to have humanoid robotic bodies?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics,check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)
  - [**HotChips 25! - everything of note**](#hotchips-25-everything-of-note)
  - [**Yet another switch from Broadcom - scaling across with Jericho4**](#yet-another-switch-from-broadcom-scaling-across-with-jericho4)
  - [**B30, a Datacentre-class GPU for China - but is the door closed to deliveries?**](#b30-a-datacentre-class-gpu-for-china-but-is-the-door-closed-to-deliveries)
  - [**PCIe 8.0 in the works, and we don't even have PCIe 6.0 CPUs yet.**](#pcie-80-in-the-works-and-we-dont-even-have-pcie-60-cpus-yet)
  - [**Other notable headlines**](#other-notable-headlines)

---

# This month's updates

## HotChips 25! - everything of note

HotChips is the annual industry event for high-performance silicon, with both the big and small names showcasing their advancements and plans  

## B300 GPU finally detailed

## Yet another switch from Broadcom - scaling across with Jericho4

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_chip.png)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_lineup.jpeg)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_scaleacross.png)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_ports.jpeg)

## B30, a Datacentre-class GPU for China - but is the door closed to deliveries?

## PCIe 8.0 in the works - but we don't even have PCIe 6.0 CPUs yet

Intel and AMD's next generation CPUs - supporting PCIe 6.0 - are expected to ship in 2H26, likely being followed closely by PCIe 6.0 SSDs, NICs, and more. PCIe 6.0 itself however was announced as early as 1Q22, a gap in the market for over 4.5 years from announcement to implementation. Based on the pace so far demonstrated, future PCIe generations might seem likely to take just as long to reach the markets, but there has been one major change: AI.

Keeping to their commitment to doubling bandwidth every 3 years PCI-SIG (Special Interest Group) has announced PCIe 8.0, aiming for up to 1TB/s bi-directional bandwidth over a x16 connection. Version 1.0 of the specification is expected to be released in 2028, with the first devices expected to ship in 2029/30, 

Intel and AMDs upcming cpus will have PCIe 6.0 in 4Q25 or something, but PCIe 8.0 has just been announced for a 2028 release, bringing up to 1TB/s bi-directional bandwidth to PCIe connections.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/pcie8_speeds.jpg)

PCIe is the protocol used for various components in a server to communicate with each other. Widely used between the CPU, AI accelerators, network cards, storage, and more.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/pcie8_doubling.jpg)


PCIe 8.0 doubles the data rate of 7.0, reaching 256GT/s per lane. 
* 256GT/s per lane
*   A lane is four wires, two each for transmitting (Tx) and receiving (Rx). GT/s is Gigatransfers per second, each transfer is 1 bit.
Almost certainly over optical, as they'll be using PAM4 signalling instead of NRZ which is reaching its limits. PAM4 is pulse amplitude modulation, using 4 levels of voltage to represent 2 bits - 2 bits can be sent within a single sybmol, which means the transfer rate required to reach the same bandwidth is halved, reducing strain on the signal generators and error rates. 




PCIe 6.0 announced in 2021, but no devices even yet. 

---

## Other notable headlines

* [Jensen Huang confirms that GTC Washington DC will reveal the Rubin GPUs as well as five other chips](https://www.tweaktown.com/news/107259/nvidia-ceo-to-visit-tsmc-in-taiwan-first-ever-gtc-in-washington-d-c-for-rubin-ai-gpu-reveal/index.html)
* [SK-Hynix to mass produce 2Tb 3D QLC NAND devices, on the path towards 244TB SSDs](https://www.tomshardware.com/pc-components/ssds/sk-hynix-announces-mass-production-of-its-2tb-3d-qlc-nand-cheaper-high-capacity-consumer-drives-and-244tb-enterprise-ssds-incoming)
* [Rumours of Nvidia's post-Rubin "Feynman" GPUs needing immersion cooling abound from industry sources](https://zdnet.co.kr/view/?no=20250818162633)
* [Samsung's HBM4 samples reportedly pass Nvidia's validation! A turnaround for Samsung in the HBM market finally?](https://m.sedaily.com/NewsView/2GWP8QI6ZB)
* [Huawei allegedly working on "AI SSDs" to reduce pressure on the Chinese HBM supply chain](https://finance.sina.cn/2025-08-25/detail-infnfiew2224904.d.html?vt=4&cid=76524&node_id=76524)
* [AMD might reveal "Venice" 6th gen CPUs and MI500X at their upcoming financial analyst day in November](https://www.tomshardware.com/pc-components/cpus/amd-to-disclose-roadmaps-in-mid-november-the-future-of-zen-6-rdna-cdna-and-udna-expected)
* [UltraRAM, tech that could store data for up to 1000 years, at DRAM speeds, is progressing towards manufacturing](https://www.tomshardware.com/pc-components/ram/ultraram-scaled-for-volume-production-memory-that-promises-dram-like-speeds-4-000x-the-durability-of-nand-and-data-retention-for-up-to-a-thousand-years-is-now-ready-for-manufacturing)
* [Nvidia announces the RTX Pro 4000 SFF and RTX Pro 2000 GPUs - Desktop grade, aimed at HPC and visualisation workloads](https://www.tomshardware.com/news/nvidia-announces-rtx-pro-4000-sff-and-rtx-pro-2000-desktop-gpus)
* [Delays in DeepSeek's R2 model allegedly due to pressure from Chinese government, being forced to use Huawei's "unstable" AI accelerators instead of Nvidia GPUs](https://www.tweaktown.com/news/107116/huawei-pressure-blamed-for-deepseeks-next-gen-ai-model-delay/index.html)
* [Kioxia confirms that they are also in the race to HBF with their prototype: 5TB capacity @ 64GB/s per "module"...](https://www.kioxia.com/en-jp/about/news/2025/20250820-1.html)
* [...But SanDisk keep up the pace by teaming up with SK-Hynix to work on standarising HBF first](https://mp.weixin.qq.com/s?chksm=c2649258f5131b4e3fa13fdac3fe6d57db83ce5e0c0a34af6ad4da969da2e1ef27add8bf5c24&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1754993167_1&mid=2247526353&sn=c8250c005cc42ad5f79a630f6a1115c6&idx=3&__biz=MzkzMTcxODM3NA%3D%3D&scene=169&subscene=200&sessionid=1754993168)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)