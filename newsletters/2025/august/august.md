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

HotChips is the annual industry event for high-performance silicon, with both the big and small names showcasing their advancements in the field. This year's event seemed dominated by relatively few players, Nvidia, Meta, and Google stealing much of the spotlight. Between all the analysts and media that attended the event, there are too many updates to cover here comprehensively, but instead we'll present some of the highlights.

### Nvidia: Spectrum-X switches and a scale-across fabric

Spectrum-X was originally Nvidia's reaction to Ethernet gaining traction after the market showed strong signs of InfiniBand lock-in fatigue. Now, rivalling InfiniBand in its adoption among Nvidia's largest customers, Spectrum-X is innovating in two key areas: massive 512-port 400T switches, and expanding beyond the confines of a datacentre.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_nvidia_3.png)

*Source: Nvidia*

On the first item, a lot was already revealed back in GTC25 in March, see [our article on this](https://sixrackunits.substack.com/i/160297922/nvidia-and-partners-announce-next-gen-datacentre-switches-with-co-packaged-optics) from then detailing almost exactly the same information. The only [new content](https://www.tweaktown.com/news/107372/nvidias-new-spectrum-x-ethernet-silicon-photonics-enters-the-chat-a-game-changer-for-ai/index.html) is some more detail on the observed (we assume) performance (according to Nvidia) of the 102T switch, and pictures of the switch that uses optical transceivers rather than the CPO version that was shown back then.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_nvidia_spectrumxgs.png)

*Source: Nvidia*

The other major reveal was the [Spectrum-XGS](https://nvidianews.nvidia.com/news/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories) add-on to Nvidia's ethernet fabric technology, a "scale-across" stack designed to connect multiple scale-out domains (datacentres) together. More on the meaning of scale-across in our article later in this post. Spectrum-XGS claims to expand telemetry, congestion control, and load-balancing all indefinitely with respect to the number of devices, and should be a lot better at reducing cross-datacentre latency where connections can be an order of magnitude or two longer than those within a datacentre.

### Google: TPUv7 and TPU racks

### AMD: Scale-up fabrics and the MI350X

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_amd_mi350x.png)

*Source: AMD*



![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_amd_scaleup.png)

*Source: AMD*

Their more scientific session was on the design of scale-up fabrics

### Meta: Catalina (NVL36x2)



### Intel: Clearwater Forest CPU

Earlier this year [we reported](https://sixrackunits.substack.com/i/169948586/the-surprising-mystery-of-diamond-rapids-leaked-tdp) on leaks regarding Intel's upcoming Diamond Rapids CPU, their "P-core" only CPU aimed at high performance AI/HPC clusters. The counterpart to the "rapids" series of CPU is the "forest" series, aimed at more scalable and less intensive workloads like virtualisation, hosting, databases and so on. For their upcoming Clearwater Forest CPU, Intel decided to go with an official reveal.

The below image summarises the specs for a dual-socket setup, so halve the quantities (except the UPI) for a single-socket setup. Though knowing the target market of these CPUs, a single-socket setup may be unlikely, as virtualisation and web/app hosting servers are supposed to be as core-dense and energy efficient as possible.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_intel_cpu.png)

*Source: Intel*

For more information, [Zartbot's article](https://mp.weixin.qq.com/s?__biz=MzUxNzQ5MTExNw==&mid=2247495152&idx=2&sn=d7e5c25374bcddaf3e302c27d7436dee&chksm=f882c3aebffeb63a3e0950965af5cdee93f030fc7958cfa650daf449e5954dcfc2ef887013d2&xtrack=1&scene=90&subscene=93&sessionid=1756236875) on WeChat and [Andreas Schilling's article](https://www.hardwareluxx.de/index.php/news/hardware/prozessoren/66880-hot-chips-2025-intel-nennt-weitere-details-zur-clearwater-forest.html) on HardwareLUXX are very detailed.

## B300 GPU finally detailed

## Yet another switch from Broadcom - scaling across with Jericho4

Scale-up and scale-out are both rapidly developing dimensions for device-device communications, though now we're beginning to see the limits of how far they can actually scale. Limits enforced not by the technology itself, but from cooling, power, and space constraints.

Racks and even rows of racks can only get so big before the distance is too great for a larger scale out domain - [signal integrity and power](https://www.silicon-line.com/copper-cable-limitations/) become too difficult to manage beyond a few meters and taking scale-up to the optical domain is incredibly expensive. Though in certain markets like China, [Huawei is showing](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/#scale-up-optics-and-no-copper) that this might not be a roadblock to adoption.

Beyond that, scale-out can cover the span of a whole datacentre with a relatively high-bandwidth fabric, but after a certain scale, switch and optics costs become difficult to justify. Clusters like [xAI's Colossus](https://www.theregister.com/2024/10/29/xai_colossus_networking/) are pushing that boundary by doubling the size of their cluster to 200,000 GPUs whilst keeping everything under a single scale-out ethernet fabric.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_chip.png)

*Source: Broadcom*

Enter Broadcom, with the 51.2T [Jericho4](https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-jericho4-enabling-distributed-ai-computing-across) "Across DC scale-out" ASIC. Aimed at long-range connections between scale-out fabrics (used synonymously with datacentre here), the Jericho4 includes many features that optimise for transport at these distances whilst maintaining a secure and lossless fabric. Fabricated with TSMC's 3nm process and using 200G SERDES

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_scaleacross.png)

*Source: Broadcom*

The main standout innovation that Broadcom advertise is the Hyperport - 4 x 800G links combined at the hardware-level into a single logical 3.2T port. This then reduces the associated overheads of managing 4 distinct ports too. This functionality has already existed for a while at the software layer with link aggregation (LAG) but Hyperport implements it lower in the stack, optimising the load balancing, congestion control, utilisation, and more.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_ports.jpeg)

*Source: Broadcom*

In addition, the Jericho4:

- Has deep buffers to absorb bursty traffic from AI workloads
- Supports lossless connections for over 100km distances
- Provides MACsec at line rate, necessary for long-distance traffic

And just to future proof it for use in 2027/28, the Jericho4 is also UEC compliant - interoperable with all other UEC switches and NICs from any vendor.

This then "completes" Broadcom's lineup of high-performance AI cluster switch ASICs, with this chip joining the Tomahawk 6 and Tomahawk Ultra to cover all three dimensions of network scaling: up, out, and across. For more information on the Tomahawk series, see our [June](https://sixrackunits.substack.com/i/167217145/broadcom-shows-the-world-a-terabit-switch-asic-tomahawk) and [July](https://sixrackunits.substack.com/i/169948586/broadcoms-inevitable-yet-surprising-new-chip-tomahawk-ultra) editions.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_lineup.jpeg)

*Source: Broadcom*

PS: It seems they'll do anything to avoid just saying "scale-across", perhaps to avoid association with Nvidia's Spectrum-XGS announcement (more on that just above)? Or maybe they were just a few days short to coining the term?

## PCIe 8.0 announced

Intel and AMD's next generation CPUs - supporting PCIe (Peripheral Component Interconnect express) 6.0 - are [expected to ship](https://www.pcworld.com/article/2805679/pci-express-6-products-might-finally-ship-in-2025.html) in between 4Q25 and 4Q26, likely being followed closely by the corresponding SSDs, NICs, and more. PCIe 6.0 itself however was announced as early as 1Q22, a wait for over 3.5 to 4.5 years from announcement to implementation. Based on the pace so far demonstrated, future PCIe generations should take just as long to reach the market from their reveal. But there's been one fundamental addition to the world driving hardware progression to speeds not seen before: LLMs.

Keeping to their commitment to doubling bandwidth every 3 years, the PCI-SIG (Special Interest Group) [has announced PCIe 8.0](https://pcisig.com/pci-sig-announces-pcie-80-specification-targeted-release-2028), aiming for up to 1TB/s bi-directional bandwidth over a full x16 connection. Version 1.0 of the specification is expected to be released in 2028, with the first devices hopefully shipping before 2032. In comparison, [PCIe 7.0](https://pcisig.com/pcie-70-specification-now-available-pci-sig-members) was announced in 2022, aims to have it's version 1.0 ratified at the end of 2025, and may see adoption in devices as soon as 4Q26. Certainly not CPUs, but possibly in NICs (already reaching 800G and soon 1.6T), and just maybe in SSDs (if storage arrays and controllers reach those speeds in time).  

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/pcie8_speeds.jpg)

*Source: PCI-SIG*

To summarise what these speeds mean, PCIe 8.0 is targeting 256GT/s (Giga Transfers per second) bidirectional (both transmitting and receiving simultaneously) per lane. [A lane](https://www.techradar.com/computing/computing-components/pcie-lanes-explained) is four wires, two each for transmitting (Tx) and receiving (Rx) and each pair is a [differential pair](https://en.wikipedia.org/wiki/Differential_signalling). A transfer is 2 bits, since PCIe 8.0 will use [PAM4](https://blog.samtec.com/post/understanding-nrz-and-pam4-signaling/) (pulse amplitude modulation with 4 levels) signalling. This means 512Gb/s per lane, or 64GB/s per lane, and therefore a x16 (full width) connection can support 16 x 64GB/s = ~1TB/s bi-directional bandwidth.

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
* [Meta working with Broadcom to get "Santa barbara" codenamed MTIA servers into production by end of 2025](https://www.datacenterdynamics.com/en/news/meta-places-order-for-its-next-gen-asic-powered-ai-servers-partners-with-broadcom-and-quanta-computer/)
* [Leaks of a possible Jaguar shores thermal test vehicle reveal a possible quad-die arrangement for Intel's last chance at the GPU market](https://wccftech.com/intel-next-gen-ai-chip-jaguar-shores-test-vehicle-surfaces-online/)
* [Japan's FugakuNEXT Supercomputer will use upcoming Fujitsu Monaka CPUs with Nvidia GPUs, adopting NVFusion tech](https://blogs.nvidia.com/blog/fugakunext/)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)