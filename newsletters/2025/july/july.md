[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# July 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/title.jpg)

**

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top and even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics,check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)
  - [**Broadcom's inevitable yet surprising new chip - Tomahawk Ultra**]()

---

# This month's updates:

## Broadcom's inevitable yet surprising new chip - Tomahawk Ultra

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/broadcom_chip.png)

*Source: Broadcom*

Announced just weeks after the 102.4T Tomahawk 6, the [new Tomahawk Ultra ASIC](https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-tomahawk-ultra-reimagining-ethernet-switch-hpc) is symbolic of Broadcom's scale-up Ethernet (SUE) overtaking UALink as the scale-up technology most capable of challenging Nvidia's NVLink. The 51.2T (512 x 100G) switch expands the performance and capability boundaries of Broadcom's existing datacentre switch lineup, with its focus on lower latencies and higher packet processing rates as well as supporting SUE's requirements such as link-layer retry and credit-based flow control.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/broadcom_ultra.webp)

*Source: Broadcom (via WeChat)*

The key number that marketing have decided to lead with is the switching latency - 250ns. It's an impressive number considering that this number for Tomahawk 5 may have been [double that](https://www.wheelersnetwork.com/2025/07/broadcom-adds-new-architecture-with.html?m=1). It should be noted however that this is purely the latency incurred from when a unit of data enters the ASIC to when it exits, and not the more important latency of getting a message from one device to another. That number still relies on other factors such as the size and priority of the message being sent, the design of the rest of the switch chassis, and any intermediate hardware such as NICs, PCIe switches, and even cable lengths for particularly long connections. This means that in or near the worst cases for latency (usually the bottlenecks for real workloads), even on the highest performing clusters, this reduction in switching latency might not make a significant difference.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/broadcom_latency.png)

*Source: Broadcom (via WeChat)*

The more surprising improvement (and probably more impactful too) though is their packet processing rate. Claiming to process [77 Billion packets per second (pps)](https://www.naddod.com/blog/broadcom-tomahawk-ultra-new-chip-for-scale-up-ethernet), Broadcom are targeting traditional HPC infrastructures too despite the majority of their marketing centering on AI. Applications such as finite difference/element models, linear solvers, or even distributed financial/trading programs are all far more sensitive to latency than AI workloads are. This has been the case for AI training for a while now, where packet sizes are usually large enough to saturate deep-buffers in higher-tier switches, and is now the norm in inferencing too, which has become almost entirely about LLMs. As a result, HPC clusters using more dense and complex topologies will benefit greatly from the high pps provided by the Tomahawk Ultra.

These dramatic performance improvements mean that the architecture of the chip has had to change a lot. The addition of more packet-processing pipelines to meet the pps requirements and compute logic to support the in-network collectives (INC) that SUE supports has resulted in the buffers needing to be smaller - and shallower - than they were in the Tomahawk 5.  As a result of all of these changes, it's technically [not really a "Tomahawk" chip anymore](https://www.wheelersnetwork.com/2025/07/broadcom-adds-new-architecture-with.html?m=1), despite its compatibility with existing sockets/boards. This doesn't - and shouldn't - matter to most though, and Broadcom's decision to label and market this chip as being in the same family as their scale-out ASICs makes complete sense.

---

## GB300 servers possibly shipping before 4Q25, "no major issues" allegedly

---

## JEDEC releases the LPDDR6 standards, samples potentially out by 4Q25

---

## The surprising mystery of Diamond rapids' leaked TDP

[The first leak](https://x.com/x86deadandback/status/1941808014865899878) was posted early this month on X from the account @x86deadandback, and drew mixed reactions from the hardware community. It provided some specs of Intel's upcoming server-grade CPU series, Diamond Rapids (DMR) (successor to the current gen. Granite rapids (GNR) series), which is expected to be formally announced in the next few months. The source themselves isn't a well established industry leaker, but the numbers given for the are believable and match expectations.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/intel_specs.jpeg)

*Source: @x86deadandback on X*

For context, the [highest performing Intel GNR SKU](https://www.intel.com/content/www/us/en/products/sku/240777/intel-xeon-6980p-processor-504m-cache-2-00-ghz/specifications.html) is advertised at 500W for 128 cores running at 2GHz base clock, and rumours suggest AMD's nex gen. ["Venice" 192 (virtual) core CPU](https://www.guru3d.com/story/amd-6thgen-epyc-venice-ccd-configuration-and-thread-performance-spotted/) will reach 600W. If the higher end AI/HPC server Intel CPUs reach 192 cores, then they will still be very competitive with their counterparts from AMD in 2026. [An earlier leak](https://x.com/x86deadandback/status/1937563563935084826) from the same source showed what appeared to be a product page or documentation specifying heat-sinks for DMR CPUs, peaking at 660W. Heat-sinks typically are rated for significantly higher output than the heat source is capable of to manage temporary performance boosts or cooling system failures, and so this specification supports the later leak.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/intel_heatsink.jpeg)

*Source: @x86deadandback on X*

To demonstrate why a 500W TDP would be so surprising, lets walk through an example server upgrade process. Even without the leak, its certain that a four-socket version of DMR will be available for CPU-dense datacentres running in-memory databases, high-performance scientific workloads, or financial transaction processing. For a site using 4096 cores spread over 64 older 64-core 350W [Emeralds rapids CPUs](https://en.wikipedia.org/wiki/Emerald_Rapids), their power usage would be 22.4kW spread over 16 quad-socket servers in two 12kW racks. To keep the minimum core count after an upgrade to DMR CPUs, that site could now buy just 22 new 192-core 500W CPUs in 6 servers, using a total of 11kW only. This could now fit into one of their 12kW racks, with capacity left for a switch or two, and the site overall has now reduced its total power usage by 11.4kW.

The example is oversimplified of course but the concept remains true: newer CPUs are generally more power efficient, and a lower TDP for the same core count can result in power, space, and cost savings if the short-term tradeoffs are acceptable. This decision is a lot easier to make when the TDP of a 192-core CPU is 500W rather than 650W. Combining this with PCIe 6.0 and CXL 3.0 support, variants with 16 memory channels, and upgraded AMX (Advanced Matrix Extensions) support [1](https://www.techradar.com/pro/want-a-quad-socket-server-with-768-cores-sure-intels-192-core-diamond-rapids-xeon-cpu-will-deliver-that-in-2026-but-i-wonder-whether-it-will-be-too-little-too-late), Intel CPUs may soon halt AMDs aggressive takeover of the server CPU market.

There's a lot more information currently circulating around the DMR series and the future of Intel CPUs in general, but they are beyond the scope of this article. For more information, see the following (perhaps more reliable) sources:
- [Discussions around Intel's statement on returning to SMT, and if DMR will also not have it](https://morethanmoore.substack.com/p/intel-ceo-letter-to-employees)
- [Another leak alleging that the DMR architecture will have shared L2 caches per core pairs](https://x.com/InstLatX64/status/1948734994798567678)

---

## H20 GPU orders pile in - Nvidia (and AMD) gains access to China again

- H20 has started selling in china again
- Specs:

- Huang visits china multiple times this year, 

- China's demand for AI accelerators will total at ~$40B by end of this year. $ companies: ByteDance, Tencent, Alibaba, Baidu account for over 80% of H20 demand. H20 still better than Ascend 910C on a chip level but its yet to be seen how the CloudMatrix384 compares in the market against H20-powered clusters. 

- Chinese AI labs will love this though, usually they run at much lower supply and tokens per second because of less infrence capacity. China is working on their own nation-spanning high-bandwdith network to help this though. Jeffereis fiance comp predicts once Nvidia sell off thier existing inventory of H20s (previously written off as ~$10B loss) then they will release a downgraded version with GDDR6 instead of HBM3. it seems Nvidia has already placed an order wtih TSMC for [more H20 units](https://www.reuters.com/world/china/nvidia-orders-300000-h20-chips-tsmc-due-robust-china-demand-sources-say-2025-07-29/), and its yet unclear if this will be packaged with HBM or GDDR. There was some drama recently with SK-hynix and nvidia talking about HBM not out of stock etc. what as this about?


- AMD also got approval for the MI308 for china. Specs as of yet unconfirmed but it may be like the H20 in that it has reduced compute to meet the second wave of AI export controls but may have newer HBM than the MI300 too, higher bandwidth!

- 5090Dv2 exists - cut down version of 5090D which was already cut down. offering 24GB of VRAM in a 600W profile, made for china. Commericial card through for retail and gamers, but needs to be under control still like the 4090s did. 
- B30 (RTX Pro 6000D) also launching in China, slower and less capable than the H20 but significantly cheaper. Given Chinese SOTA models being MoE, it seems band2idth requirements arent so crazy high and instead these cheaper multi-card systems might be quite appropriate for cheap inferencing. Supply seems to be confirmed and purchases appear to be made. GDDR7.
- China has not just acess to GPUs, but access to a diverse set of Nvidia GPUs - They are retaking the chinese market, leaving little space for domestic competitors.

Tuesday 15th July marked Jensen Huang's third visit to China in a very short span of time. Discussions on plans to sell in china as export restrictions are eased, allowing Nvidia's H20s to be sold in China again. H20s are the second generation of watered down H100 chips, to meet the restrictions imposed on compute capability and bandwidth. When the H20s were banned for sale in <DATE?> NVidia had to write off its existing inventory as a loss of ~$10.5B. 

However now with the xport controls eased, Nvidia expects to ship X units per quarter in 2025, and when supply runs out, it seems NVidia has contracted TSMC for additional units. Though these may end up using GDDR6 instead of HBM3, lowering the performance possibly. 

But given what chinese labs need, they may still be a very attractive options. Currently struggling to get inferencing speeds for their models up, need supply of any GPUs badly. B30s will also fill gaps for lower perf but better cost. AMD MI308 is also shipping to select customers but in much lower volumes due to the dominance of CUDA in china still. Perf unknown but given the limits applied to H20 in bw and perf, we can expect something similar. Nvidia also aiming at commercial cards with 5090Dv2. 

This fiversity of newly available GPUs across the performance vs cost space now hurts many domestic competitors and manufacturers like Huawei and others. Though its yet to be seen how their cluster-solutions match against what will be available in china which wont be NVLs but relatively weakly networked servers. 



[5090Dv2](https://www.tweaktown.com/news/106572/nvidias-new-geforce-rtx-5090-v2-launches-in-china-on-august-12-24gb-vram-600w-tdp/index.html?utm_source=newsletter&utm_campaign=newsletter)
[b30 shipping Q4, slower but cheaper](https://www.tweaktown.com/news/106517/nvidias-new-b30-ai-gpu-planned-to-ship-in-q4-10-20-slower-than-h20-but-30-40-cheaper/index.html?utm_source=newsletter&utm_campaign=newsletter)
[bernstein chip demand, main 4 buyers in china](https://x.com/Jukanlosreve/status/1947075312694722707?t=syNSPYJTvzyoZZ6IcXFz9w&s=09)
[Chinese labs server slower speeds, now exanpd with H20s](https://techzephyr.substack.com/p/implications-of-h20-coming-back?triedRedirect=true)
[Nvidia to sell existing h20s first, then GDDR6 version. Demand could reach 1 million units per quarter](https://x.com/Jukanlosreve/status/1945652728795136033?t=9lBAsHca2W5IssU0XtQVAw&s=0)
[Huang third visit to china, 2 million 6000Ds](https://www.digitimes.com/news/a20250715PD201/nvidia-jensen-huang-rtx-us-china-trade-war-2025.html?chid=10)
[TSMC new 300000 H20s](https://www.reuters.com/world/china/nvidia-orders-300000-h20-chips-tsmc-due-robust-china-demand-sources-say-2025-07-29/)
[H20 specs](https://mp.weixin.qq.com/s?__biz=MzkxMDIzMDMzNQ==&mid=2247483902&idx=1&sn=cc8b29b41c6ba920abe59eb669054f30&chksm=c0cab17d69f45c8b36c37227346061e559685bbd2c34692c157e140067f28b0a5f96ea408c1d&xtrack=1&scene=90&subscene=93&sessionid=1752602682)
[mi308 approved](https://www.bloomberg.com/news/articles/2025-07-15/amd-says-it-will-restart-mi308-sales-to-china-after-us-review?embedded-checkout=true)
[6000D using GDDR7, samsung supplying HBM3 for H20s](https://www.trendforce.com/news/2025/07/15/news-nvidias-china-h20-sales-to-resume-after-u-s-commitment-samsung-poised-to-gain-from-hbm3-supply/)


---

## Other notable headlines

* [Samsung may supply HBM4 samples to AMD, Nvidia, and others by end of this month...](https://mp.weixin.qq.com/s?__biz=MzUzNTI5MTg3NA==&mid=2247485277&idx=1&sn=87490e5877da966181e0b765783bd76b&poc_token=HLOWgmijKey9o-fT9lAP_wGWGOj-DZZtaBWvlD0f)
* [...But mass production may end up starting in 2026 after all](https://www.digitimes.com/news/a20250724PD223/samsung-hbm4-production-2026-sk-hynix.html#:~:text=Report%20SCMP%20Bundle-,Samsung%20delays%20HBM4%20rollout%20to%202026%20due%20to%20yield%20challenges,strengthens%20lead%20in%20AI%20memory&text=Samsung%20Electronics%20is%20reportedly%20pushing,amid%20ongoing%20DRAM%20redesign%20efforts.)
* [NVidia brining CUDA to RISC-V machines - but maybe RISC CPUs only, not GPUs](https://xpu.pub/2025/07/23/cuda-risc-v/)
* [Huawei to display the CloudMatrix384 in person, live, at the end of this month at WAIC25](https://money.udn.com/money/story/5603/8882141)
* [Against all odds, smugglers find a way to get GB200 racks into China - on sale now](https://www.tweaktown.com/news/106623/nvidia-gb200-ai-servers-smuggled-into-china-despite-their-two-ton-weight/index.html)
* [HBM4 is coming](https://www.hbm4.org/)
* [Tesla to use TSMC for its Dojo 3 chip](https://www.ctee.com.tw/news/20250725700068-430501)
* [Intel's next-gen desktop CPUs, "Titan Lake" possibly scrapping P/E-core split, moving to unified cores](https://www.trendforce.com/news/2025/07/18/news-intel-reportedly-drops-hybrid-architecture-for-2028-titan-lake-go-all-in-on-100-e-cores/)
* [Huawei may move to a more GPU-like architecture for the future of its Ascend series AI accelerators](https://x.com/kyleichan/status/1943879673382867403?t=_jO4qxORFtzyS6FsfP6Zpw&s=09)
* [AI accelerator startup Furiosa wins a significant customer in Korea - LG Electronics](https://www.theregister.com/2025/07/22/sk_furiosa_ai_lg/)
* [SK-Hynix confirms 3GB GDDR7 modules in development](https://www.tomshardware.com/pc-components/gpus/sk-hynix-confirms-3gb-gddr7-memory-modules-are-in-the-works-higher-capacity-could-pave-the-way-for-fabled-rtx-50-series-super-cards-with-24gb-vram)
* [Samsung awared $16B contract for Tesla's AI6 2nm chips over 8 years](https://www.theregister.com/2025/07/22/tesla_ai6_2nm_chip_contract/)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)