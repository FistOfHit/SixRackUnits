# February 2025

![Could hardware ever reach a point of density and efficiency such that all computation happens locally and is P2P only? Or would the demand for compute scale endlessly with its supply?](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F119de8c8-0e8b-4b27-9cc4-c3a4bd6550a2_2688x1536.png)

*Could hardware ever reach a point of density and efficiency such that all computation happens locally and is P2P only? Or would the demand for compute scale endlessly with its supply?*

**This month's updates:**

* SanDisk develops "high-bandwidth flash" memory, aiming for TB capacity on GPUs
* Meta reportedly looks to acquire Korean chip startup FuriosaAI
* Updates on the Nvidia B300 "Ultra" and Rubin series
* Intel's roadmap and its dependence on 18A
* Huawei to challenge Nvidia's dominance in China with the Ascend series
* Other notable headlines

**Vendor spotlight:**
* NextSillicon

**One-pagers:**
* Racetrack memory
* Baseboard management controllers

---

# This month's updates:

## SanDisk develops high-bandwidth flash (HBF) memory

*High bandwidth memory (HBM) is one of the most important components of AI accelerators, enabling the massive amounts of rapid memory transfer needed for AI training workloads, but this performance comes at cost: DRAM - which makes up HBM - is expensive and takes up a lot of area per unit of storage. SanDisk, however, might just have solved this with HBF.*

Regular DRAM struggles to saturate the bandwidth demand from AI accelerator compute elements, necessitating the development of technologies like LPDDR/X (low-power DDR/enhanced), GDDR (Graphics DDR), and HBM (High bandwidth memory). While implementation details vary greatly, there is one major common foundation they all share: DRAM. By design, DRAM strikes a balance between power use, density, and cost, leading to it being the best solution for on-device memory that lives just outside the processor but still closer than any larger capacity storage.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20b01bbb-4d18-4c2e-b9ca-d44502fad46e_409x263.png)

*Source: SanDisk*

SanDisk, having just completed their [spin-off](https://www.sandisk.com/company/newsroom/press-releases/2025/sandisk-celebrates-nasdaq-listing-after-completing-separation) from Western Digital, have announced a possible solution that could combine the large capacities of flash storage memories such as SSDs with the bandwidth that HBM provides to the processor - [HBF](https://www.tomshardware.com/pc-components/dram/sandisks-new-hbf-memory-enables-up-to-4tb-of-vram-on-gpus-matches-hbm-bandwidth-at-higher-capacity). At their annual [investors' day presentations](https://shop.sandisk.com/en-gb/company/newsroom/press-releases/2025/sandisk-investor-day-2025), SanDisk revealed how they've prototyped a vertical stacking technology (just as HBM does with DRAM) to combine multiple flash memory dies into a single, high-throughput design that can meet the TB/s bandwidth requirements from HBM devices whilst providing the hundreds of GB of capacity enabled by higher density flash memory.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03346542-f35f-42be-9015-36b09ec11a0f_1405x750.png)

*Source: SanDisk*

Whilst they admit that latency will still be worse than DRAM-based memory, SanDisk show how AI hardware designers could combine HBF and HBM to have smaller volumes of fast access memory acting as another level of cache, and the higher capacity HBF acting as a higher level of warm storage that can keep data on device - avoiding the [10-100x relative cost](https://www.techtarget.com/searchstorage/answer/What-is-the-difference-between-cache-memory-and-RAM-cache) of fetching data from the host server. The first generation of HBF is expected in 2H25 providing up to 500GB of capacity per stack, with the second (2026) and third (2027) generations increasing capacity further up to 1TB per stack and attempting to keep up with the bandwidth we can [expect from HBM4](https://www.supermicro.com/en/glossary/hbm4).

## Meta to acquire Furiosa

*South Korean chip designer Furiosa has gained recognition recently for its innovative and efficient RNGD (pronounced "renegade") tensor-contracting processor, aiming to compete with Nvidia in AI training and inferencing. Now, analysts report that Meta is already in late-stage discussions to acquire the startup and add to its own custom silicon roadmap.*

Industry analysts [report](https://www.kedglobal.com/mergers-acquisitions/newsView/ked202502120005) that the acquisition could be completed as early as by the end of this month, but looking at clues in papers released on the technology Furiosa implement, it's possible that Meta (then Facebook) were [collaborating](https://par.nsf.gov/servlets/purl/10099301) with the startup's technical team as far back as 2019. The buyout would likely lead to Meta mixing their development teams with Furiosa's and incorporating future products into its existing custom silicon lineup, as Meta presently deploys two generations of their "Meta Training and Inference Accelerators" - [MTIAs](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/) - for their ranking and recommendation systems that run their services on apps such as Facebook and Instagram. From a 2024 [leaked internal memo](https://www.techradar.com/computing/virtual-reality-augmented-reality/leaked-meta-memo-calls-2025-a-make-or-break-year-for-reality-labs-but-multiple-new-ai-smart-glasses-and-mixed-reality-apps-could-be-coming-to-save-it), it appears that Meta already had plans for the next generation of their AI accelerator in 2025. Whether this plan included the merging in of Furiosa's roadmap is unclear.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71e82713-24d8-4b4c-96e8-ca52a8f40861_444x194.png)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52010258-8b54-4b51-a7b4-75f63d9bbb46_449x211.png)

*Source: Furiosa*

Furiosa released their second processor, the [RNGD](https://furiosa.ai/rngd), in 2024 - a PCIe form factor server chip targeting LLM training and inference providing ~1.6-2x the efficiency of Nvidia H100s on inferencing models in the 6-8B parameter range. The success of their accelerators is down to two key innovations: a tensor contraction compiler ([1](https://par.nsf.gov/servlets/purl/10099301) [2](https://dli5ezlttyahz.cloudfront.net/FuriosaAI-tensor-contraction-processor-isca24.pdf?p=download/FuriosaAI-tensor-contraction-processor-isca24)), and a tensor contraction processor. [Tensor contraction](https://en.wikipedia.org/wiki/Tensor_contraction) is a higher dimensional generalisation of matrix multiplication, and the compiler's success comes down to optimising memory layout and caching for better read/write patterns. All of this is then enabled by the unique processor design which performs dot-product operations on variable data shapes. All this results in a CGRA-like architecture designed for [variable tensor input sizes](https://furiosa.ai/blog/is-furiosas-chip-architecture-actually-innovative-or-just-a-fancy-systolic-array), more so than even Google's systolic array based TPUs.

As for its specs ([1](https://furiosa.ai/renegade-spec) [2](https://furiosa.ai/blog/bringing-hbm3-to-rngd-key-challenges-and-benefits) [3](https://www.linkedin.com/posts/cfregly_furiosaai-tensor-contraction-processor-isca24-activity-7295524407366557697-8FHN/) [4](https://www.koreatimes.co.kr/www/tech/2025/02/129_392093.html)):

* Using TSMCs 5nm process node
* PCIe dual-slot FH 3/4L form factor
* 256MB on chip SRAM (384TB/s)
* 256TFLOPS at BF16
* 150W TDP air cooled
* 2 x 24GB 12-hi HBM3 (likely SK-Hynix)
* 48GB of 12hi HBM3 (1.5TB/s)
* 1GHz TCP frequency
* Supermicro server integration
* $10,000 (analyst estimate)

## GB300 "Ultra" and Rubin series

*As Nvidia's B200 rack-scale SKUs start coming online on cloud platforms, more leaks and unofficial reports begin to surface on the next two generations of AI GPUs. The B300, successor to the B200 and previously known as the "Blackwell Ultra", and the upcoming architecture named "Rubin" have made headlines for changes to their specs and release dates.*

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F779bbc2c-16c3-4854-bb64-a6089f0faeb1_1297x886.png)

*Source: SemiAnalysis*

Though rumours circulated as early as 2Q24, it's now been [confirmed](Though%20rumours%20of%20this%20circulated%20as%20early%20as%202Q24,%20it's%20now%20been%20all%20but%20confirmed) that Nvidia will reveal the B300 at their annual GTC conference in March. The B300 is reported to launch in 3Q25 for sampling and then go into mass production as early as 4Q25, using 288GB of SK-Hynix's 12hi HMB3E on a TDP of 1200W. For the scale-out networking, the B300 and the Grace CPU-enabled GB300 trays will come with [ConnectX-8 NICs](https://resources.nvidia.com/en-us-accelerated-networking-resource-library/connectx-datasheet-c) capable of 800Gb/s optical connections over a single OSFP or dual-QSFP112 ports. It should be noted that CX8 NICs will be both SpectrumX (Ethernet) and QuantumX (InfiniBand) capable, removing the need for expensive and power-hungry [BlueField superNICs](https://resources.nvidia.com/en-us-accelerated-networking-resource-library/datasheet-nvidia-bluefield?ncid=no-ncid) where customers required Ethernet E/W networks. Just as [SemiAnalysis reported on Christmas day](https://semianalysis.com/2024/12/25/nvidias-christmas-present-gb300-b300-reasoning-inference-amazon-memory-supply-chain/), the G/B300s will still be sold as a rack in the NVL72 form-factor. Finally, Nvidia recognised the logistical bottleneck caused by the SXM baseboard design and evidence confirms that they are switching to a socketed design ([1](https://substack.com/profile/104007562-hitesh-kumar/note/c-96816295?utm_source=notes-share-action&r=1px8qy) [2](https://mp.weixin.qq.com/s?chksm=88682751bf1fae4732fea02648819d9a5aa0f97a8372fe9c7fadc0f1e33f26a2bdba4dd3a045&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1740476660_1&mid=2649353786&sn=d19ed1778f3d124596b080b70b46c71d&idx=1&__biz=MzA5MTg5Nzg2MA%3D%3D&scene=169&subscene=200&sessionid=1740476657&flutter_pos=9&clicktime=1740476671&enterid=1740476671&finder_biz_enter_id=5&ascene=56&fasttmpl_type=0&fasttmpl_fullversion=7618092-en_US-zip&fasttmpl_flag=0&realreporttime=1740476671813&devicetype=android-35&version=28003843&nettype=WIFI&lang=en&session_us=gh_5964496a8bcd&exportkey=n_ChQIAhIQnKsd2IzfTCJbuE3Lx2g6mBLtAQIE97dBBAEAAAAAAG50KOkTF6oAAAAOpnltbLcz9gKNyK89dVj0U36TPhynVzbX8wqi0qqNmakq89woPg2ImC%2BUZH7OS5DjDIT01A0zDVvlS3R3SOLgfyuAPapX1mk0S8Lbl5G17B7qt8cGkg%2F13zMsxig4dsAFwA83qrOH2qHxIMOD8Pg2YvAD9TysyN3yI%2FE%2BVkKm6hBn75D%2B4XQP81ZXv1vGHm87%2Ff%2F3QzP6RxrqXVC%2B%2B6jFS8rEa7SZchKxNRnXq%2BD7Jh6M1hCHdm0KiBcNm1QH2U65HqWUIUrqEYbJbCmGpn7c%2Bl%2BiYtmBWA%3D%3D&pass_ticket=FRBY%2F4PbI3uvcJQ5bu4LQJSOL5zIW9qnZ53cbZbclOxKaFUkeTva%2BqG3f9ycaNM1&wx_header=3)) using removable "SXM pucks", enabling other OEMs and integrators aside from Wistron and Foxconn to manufacture and maintain the baseboards.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbddfd4e2-2350-48a2-9e15-0185af733fb5_2166x882.png)

*Source: SemiVision*

As for Rubin, the next architecture in Nvidia's roadmap after the Blackwell series, [sources](https://zdnet.co.kr/view/?no=20250115092519) now state that it may launch for sampling as early as 2H25 because of memory maker SK-Hynix's rapid progress with their sixth-generation HBM4 memory technology which will enable the Rubin series GPUs. How this accelerated release date impacts orders for Nvidia's G/B200 and B300 rack-scale SKUs, and whether a whole generation of networking technology will be skipped is yet unclear. Further, it appears certain now that Nvidia will announce a 4x increase in GPU/rack density with the Rubin NVL288 ([1](https://substack.com/home/post/p-157788904?utm_campaign=post&utm_medium=web) [2](https://x.com/asiatechwire/status/1885583806482309608)), a single, possibly 1 megawatt rack-scale SKU using an orthogonal backplane (fixed socket-like connectors) for power delivery and switching as well as direct-to-chip liquid cooling.

## Intel's roadmap and its dependence on 18A

*Intel's roadmap on AI accelerators has changed so frequently in recent years that some large customers interested in the Gaudi series decided to stick with vendors able to provide more maintainable and upgradeable product, but recent successes with their 18A process node and PC/server CPUs might finally turn things around.*

After recent rumours of [possible selloffs](https://www.investopedia.com/intel-stock-jumps-following-fresh-reports-of-possible-broadcom-tsmc-deals-11681284) of parts of the business to market rivals, it appears Intel is now pinning its future (or at least its independence) on the success of the 18A (1.8nm) process node - Intel Foundry Service's (IFS) "greatest transistor innovation in a decade". Its success relies on [two key advancements](https://www.intel.com/content/www/us/en/foundry/process/18a.html): the RibbonFET (field effect transistor) and BSPD (back-side power delivery). The new RibbonFET design, based on the same fundamental architecture as arch-rival TSMC's [gate-all-around](https://www.asml.com/en/news/stories/2022/what-is-a-gate-all-around-transistor) (GAA), brought significant performance gains compared to the "Intel 3" 3nm and now aims to match the capability of [TSMC's "N2"](https://www.digitimes.com/news/a20240115PD215/tsmc-gaa-2nm-2025.html) 2nm. In addition, BSPD uses the back (or underside) of the silicon wafer for power delivery, leaving the front (or top) for logic. This results in better utilisation of chip area due to not having to mix power and transistor elements on one surface, as well as lower power leakage due to wires being able to be thicker and shorter. For memory, [both TSMC and Intel](https://x.com/IanCutress/status/1892246045385515266) now offer ~38 Mbit/mm^2 of memory density in SRAM - a type of memory which is used almost everywhere on chip, in registers, buffers, caches, and more.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f4b9ab8-9062-4b3b-a3b6-429678966dd3_294x255.png)

*Source: Intel*

Despite the technological advancements, it seems that there are still significant challenges ahead until 18A earns Intel some semiconductor manufacturing market share from customers using TSMC and Samsung. Due to [release in 2H25](https://www.trendforce.com/news/2025/01/07/news-intel-confirms-panther-lake-first-processor-manufactured-with-18a-node-to-launch-in-2h25/), Intel's Panther Lake desktop CPU has been subject to industry leakers who report on both the yield rate of the processor manufacturing process, and the performance of the processors cores. [One source](https://x.com/mingchikuo/status/1894054674384523347) states that rate is as low as 20-30%, a number at which mass production would be incredibly difficult if not impossible. There have been no statements yet on whether Panther Lake may be delayed or cancelled, and samples have [already been sent out](https://www.hostzealot.com/blog/news/problems-with-intel-panther-lake-processors-became-apparent-before-the-release) to select customers. [Another source](https://wccftech.com/intels-18a-process-shows-great-performance-as-panther-lake-socs-are-finally-up/) claims that the performance of the CPU's "P" or performance cores (optimised for high throughput rather than energy efficiency) is "average", indicating that the numbers from whatever benchmarks were run might not be competitive with other similar products on the market. These leaks appear to have some merit however, as rumours are already circulating hinting at the ~2026 Nova Lake (successor to Panther Lake) using a [mixture](https://www.pcgamer.com/hardware/processors/intels-next-gen-desktop-cpu-nova-lake-allegedly-spotted-and-cant-come-soon-enough/) of Intel's planned 14A process node and TSMC's N2.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee0f5e46-31f4-429d-97ed-3f05bc345517_348x278.png)

*Source: Intel*

## Huawei's Ascend series

*Chinese semiconductor manufacturer SMIC, once struggling with 7nm, is now likely testing its 5nm process with possible yield rates between 30-70% on Huawei's yet to be announced Ascend 920 or 910D AI GPU. If the improvement on the 910C is large enough, it's possible Huawei may capture a significant share of the Chinese market from Nvidia.*

Chinese chip makers appear to be catching up with TSMC/Intel with rumours ([1](https://x.com/tom335363/status/1884665291373752753) [2](https://mp.weixin.qq.com/s?chksm=c2448fccf53306dab51896894d6502234d04cf1e49ea39a4693df7b83aec8f37886c6e36dabe&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1740301411_2&mid=2247483955&sn=0c1f259d598fbc673ddf39d44048392a&idx=1&__biz=MzkzMzg3ODkyOA%3D%3D&scene=169&subscene=200&sessionid=1740301411&flutter_pos=18&clicktime=1740301605&enterid=1740301605&finder_biz_enter_id=5&ascene=56&fasttmpl_type=0&fasttmpl_fullversion=7613997-en_US-zip&fasttmpl_flag=0&realreporttime=1740301605741&devicetype=android-35&version=28003843&nettype=WIFI&lang=en&session_us=gh_9a7e64905b77&exportkey=n_ChQIAhIQrU7aMnLtgmdSDakOaHo4gRLtAQIE97dBBAEAAAAAANcdEEK8ITsAAAAOpnltbLcz9gKNyK89dVj0AO7CgmlMQELBIWDr8%2BqaU5VZ0H7j50B%2Bt%2FttFXEtVqrnFU0EL6i3TjEJYnV%2FYbmzkSrTU4JxMT%2BQfQfVI%2FFYNRpZ250FOXiHFsUdEaafDQnNWsRSjThvaS98I69spcQaCmv%2FZ47kUeKY35IXWeCNusb1%2BIMu%2BCTEiYkgf9GdUhCzVre%2F4PH%2FhrTxLPuhD2CpS2k%2BTE7yavc6RJ04xOCNf3IMkR25Dn3ubR0R7g840znasx2c9G9Hc%2ByH7mZQTL8tbn4IX0HIBw%3D%3D&pass_ticket=%2BdewM9ZmTnThQdzgwRR1rZymgsqtJR4Tm7zH%2FoEKsSBEXPAptWoWYcKvbQ%2BS67yZ&wx_header=3) [3](https://asiatimes.com/2024/02/smic-to-sell-huawei-costly-inefficient-5nm-chips/) [4](https://www.tomshardware.com/tech-industry/semiconductors/chinas-smic-foundry-on-track-to-produce-5nm-smartphone-chips-for-huawei-this-year-report)) of SMICs 5nm process node now showing acceptable yield rates of somewhere between ~30-70%. The two U.S. CHIPS acts implemented in [2021](https://www.forbes.com/sites/georgecalhoun/2021/11/23/semiconductors--the-chips-act-why-it-is-what-it-is-part-1/) and [2022](https://en.wikipedia.org/wiki/CHIPS_and_Science_Act) prevented Nvidia from [selling its AI hardware](https://www.theguardian.com/world/2022/sep/01/us-blocks-sales-of-some-ai-chips-to-china-as-tech-crackdown-intensifies) and ASML from [selling chip manufacturing equipment](https://www.theregister.com/2022/07/05/us_expands_efforts_to_hamstring/) to China, but instead of stalling progress as intended, the legislation may have instead resulted in accelerating the nation's independence in the semiconductor space. Various tech giants are already running workloads on the original 910 and the second generation 910B (the latest publicly available AI GPU from Huawei) with names such as [ByteDance](https://www.huaweicentral.com/bytedance-ordered-100000-huawei-ascend-910b-chips-to-replace-nvidia/), [Baidu](https://www.huaweicentral.com/whats-the-ascend-910b-ai-chip-baidu-ordered-from-huawei/), and most recently even [DeepSeek](https://www.gizchina.com/2025/01/30/why-did-deepseek-switch-from-nvidia-chips-to-huawei-for-running-the-r1-ai-model/) likely using large clusters of both 910/910B servers for their inferencing workloads. In terms of packaging and integration, Huawei presents their AI GPUs in the typical 8 GPU configuration, with networking topologies within servers being a 2x4 mesh, and between servers being a fat-tree topology, differing significantly from rivals such as Nvidia and AMD.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad339e65-1c6e-48ac-add6-bd457389ffde_273x223.png)

*Source: Huawei*

The [920](https://www.asiafinancial.com/huawei-smic-set-to-defy-us-sanctions-with-5nm-chips-ft) (or [920C](https://www.gizchina.com/2025/01/30/why-did-deepseek-switch-from-nvidia-chips-to-huawei-for-running-the-r1-ai-model/), or [910D](https://x.com/tom335363/status/1884665291373752753), to be confirmed), the successor to the still only privately tested 910C, is [rumoured](https://x.com/zephyr_z9/status/1885691835362029821) to be available to some customers for sampling in 3Q25 and ready for mass production in ~2026. [Sources](https://www.tomshardware.com/tech-industry/semiconductors/chinas-smic-foundry-on-track-to-produce-5nm-smartphone-chips-for-huawei-this-year-report) suggest that Huawei will use SMIC's 5nm process for the 920 depending on how it performs in making their Kirin mobile chip. As for the 920's specs, it's impossible to even speculate given that most of the information on the 910C is still unofficial. Leakers and independent analysts suggest various numbers from the 910C having between [96](https://www.nextplatform.com/2024/08/13/huaweis-hisilicon-can-compete-with-nvidia-gpus-in-china/) and [128](https://x.com/zephyr_z9/status/1885691835362029821) GB of HBM, to having either [256](https://www.techinsights.com/vendor/huawei) or [512](https://www.nextplatform.com/2024/08/13/huaweis-hisilicon-can-compete-with-nvidia-gpus-in-china/) TFLOPS of FP16 compute, but the reliability of the sources varies greatly. Despite the impressive performance of the 910C, Nvidia's sanction-busting H20 GPUs (the H100, but with less compute and slightly better memory) have seen [major orders placed](https://www.reuters.com/technology/artificial-intelligence/nvidias-h20-chip-orders-jump-chinese-firms-adopt-deepseeks-ai-models-sources-say-2025-02-25/) in 1Q25, after the Trump administration hinted at [further iterations](https://www.reuters.com/technology/trump-prepares-change-us-chips-act-conditions-sources-say-2025-02-13/) of the CHIPS act.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1d1e4b2-de6b-4e5c-a15d-88cb67879452_1111x615.png)

*Source: Huawei*

## Other notable headlines

* [Samsung reportedly redesigns its 1c DRAM process node to tackle low-yield issues, likely preparing for HBM4 in 2H25](https://www.tomshardware.com/tech-industry/artificial-intelligence/exacluster-with-144-nvidia-h200-ai-gpus-detailed-by-its-designer-hydra-host-enters-the-scene)

* [Nvidia working with all major memory makers on new "SOCAMM" memory for AI PCs, based on LPDDR5X](https://www.tomshardware.com/pc-components/dram/nvidia-reportedly-developing-socamm-memory-standard)

* [Samsung to launch new low-power, low-latency, wide I/O DRAM (LPW/LLW DRAM) in 2028, aiming at providing HBM to mobile devices](https://www.tweaktown.com/news/103362/samsung-to-launch-next-gen-lpw-dram-for-on-device-ai-in-2028-touted-as-mobile-hbm/index.html)

* [Japanese AI lab Sakana.ai releases AI CUDA engineer, a system for writing optimised code to improve GPU performance – would help develop even better AI models](https://sakana.ai/ai-cuda-engineer/)

* [Microsoft releases the Majorana 1 – an 8-qubit quantum computer using a new state of matter to perform computations, enters the quantum race with Google and IBM](https://www.servethehome.com/microsoft-majorana-1-topological-qubit-quantum-computer-shown/)

* [SK-Hynix achieves 70% yield in 12hi HBM4 ahead of mass production, possibly leading to Nvidia accelerating their own timeline for the Rubin series](https://www.trendforce.com/news/2025/02/27/news-sk-hynix-fast-tracks-hbm4-development-reportedly-hits-70-yield-in-12-layer-testing/)

* [Samsung to use Chinese YMTCs technology for 400+ layer NAND flash SSDs](https://www.trendforce.com/news/2025/02/24/news-samsung-rumored-to-adopt-hybrid-bonding-patent-from-chinas-ymtc-for-400-layer-nand/)

---

# Vendor spotlight:

## NextSilicon

*One of the few chip designers aiming at scientific compute, [NextSilicon](https://www.nextsilicon.com/) develops "intelligent compute accelerators" (ICAs) that optimise for natively running C++ and Fortran workloads at efficiencies and throughputs/latencies unmatched by CPUs and GPUs. Their "Maverick" ICA now looks to prove itself and break into the datacentre server space.*

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9fd935b-9ea5-4d02-88cb-e190a7c5a569_445x296.png)

*Source: NextSilicon*

Founded in 2017, Israeli startup NextSilicon differentiates itself from the competition in [two key ways](https://www.nextsilicon.com/maverick): the target market they pursue, and their requirement to support existing target workloads. Their products aren't aimed at accelerating AI but instead at regular scientific compute workloads that have been - and still are - the biggest consumers of compute in the world. Applications that would benefit from NextSilicon's designs include weather forecasting, finite element analysis, and graph algorithms, all of which rely on structured and repeatable computations on data but with less predictable memory access patterns and more varied control flows. Almost all such applications are written and maintained in two programming languages, C++ and Fortran, both in use for decades for building highly performant programs that run much of the world's software today. NextSilicon aim to keep it that way by ensuring their "[software-defined hardware](https://www.nextsilicon.com/tech)" runs such applications natively, with no need for porting to another language or writing intermediate representations, which is what vendors like [Nvidia](https://en.wikipedia.org/wiki/CUDA), [AMD](https://en.wikipedia.org/wiki/ROCm), and [Intel](https://en.wikipedia.org/wiki/OneAPI_\(compute_acceleration\)) require when using their specialised accelerators.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d1b5cd2-bf57-4ef2-86c5-c5ed0f5f90d3_480x334.png)

*Source: NextSilicon*

Their novel processor, the [Maverick](https://www.nextsilicon.com/maverick), now in its second generation, introduces software-defined hardware acceleration by taking scientific applications in their [native forms](https://www.nextsilicon.com/insights/BYOC_maverick2_blog) (just as they would run on CPUs) and learning what the software requires from hardware to run optimally. It does this by running them on its own dynamically reconfigurable grid of general purpose "E-cores" and math-specialised "compute elements" and building graphs of the various paths data takes as it moves from memory, through the compute, and back to memory. It then reconfigures itself on the fly to best suit those computational graphs and accelerates application performance by up to 4x when compared to GPUs and 20x compared to high-end CPUs. [As for specs](https://www.nextsilicon.com/maverick), the Maverick 2 in its 300W-TDP PCIe form factor provides up to 32 E-cores and 224 compute elements, along with four stacks of HBM3E, totalling at 96GB. The OAM version supports two compute die and up to 192GB of HBM3E but has a TDP of 600W, requiring liquid cooling. Both forms are built on TSMCs 5nm process.

---

# One-pagers:

## Racetrack memory (RTM)

*Device memory is usually stored as electric charge across a capacitor or as a state of a set of transistors, however magnetism provides a new way of complementing or replacing SSDs or DRAM with a low latency/jitter, energy efficient, and non-wearing solution: RTM, which stores information between magnetic domains in nanowires shows promise.*

Originally developed by researchers at IBM and now in the experimental stage with various other institutions, RTM aims to combine the high performance and reliability of solid-state memory with the cost-effectiveness and density of traditional magnetic storage. RTM, unlike conventional memory which stores information in transistors and capacitors, uses "racetracks" or nano wires that hold multiple magnetic regions separated by thin domain walls or gaps. These domain walls represent the information to be stored, and information is moved from storage to read/write heads by shifting the magnetic domains up and down the wire using electrical currents.

The shifting action, as well as how quick and efficient it is to read and write information to the wires, leads to the potential for RTM to become part of future memory devices. Additionally, unlike flash storage which requires distinguishing charge levels in a capacitor that wears out over time, racetrack nanowires do not degrade with use. The use case and capabilities of RTM-based memory depends on its structure and the design of the device, just as with flash and DRAM based technologies. Whether the wires are arranged in two- or three-dimensional arrays, how many read/write heads are used to get and store information in parallel, or how error correction is optimised for shift-based memory movement all influence where and how RTM can be used and what advantages/disadvantages it presents.

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4c44a37-cec5-41d1-b94f-9f67e51a8e09_348x369.png)

*Source: IBM*

AI workloads - now the fastest growing use case for high-performance hardware - could potentially see significant improvements in throughput/latency and flops/watt with processors using RTM. With compilers that can breakdown high-dimensional matrix operations (most of what AI models do internally) into instructions suited to reading and writing from arrays of racetracks, hardware that utilises RTM to compliment or replace DRAM-based memory could theoretically lead to large improvements in performance. Currently, IBM appears to be the industry leader in RTM research, and many universities experimenting independently on their own prototypes.

## Baseboard management controllers (BMCs)

*A baseboard (or motherboard) hosts all the components of a server and connects them via copper wires or sockets and cables. The microcontroller which manages much of the state and functionality of the board is known as the baseboard management controller (BMC) and is one of the most important yet often overlooked parts of a server.*

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59cdc876-48ad-428e-8d85-df5645b4ec4d_2073x1186.png)

BMCs are dedicated chips on the baseboard that perform a variety of functions crucial to managing a server. Primarily, they enable out-of-band (OOB) management through their own dedicated network interfaces, allowing administrators to remotely power-cycle servers, update BIOS/UEFI firmware, or diagnose failures even when the host operating systems are unresponsive. Modern BMCs are usually built on ARM or RISC-V architectures - even in x86 servers - but operate independently from the CPUs and draw power through their own separate rails. For temperature and power management they interface with thermal sensors, voltage regulators, and fans/other cooling systems, and so can modify power supply/frequency to components to enforce programmable temperature limits. To interact with a BMC directly, most manufacturers provide APIs to expose key functions. The industry standard that has emerged over the past decade is Redfish, which provides ways to interact with the BMC through POST/GET calls, Python, and Ansible to name a few.

As servers tend towards hundreds of cores per CPU, multiple GPUs, and additional NICs/switches all on the same board, the demand on the BMCs increases super-linearly. Individual components become denser and more performant with every iteration, but the number of sensors and the frequency of incoming data also increases, resulting in an even greater load on the management controller and connections. This trend towards increased networking and processing load has resulted in BMCs having a higher core count and using high-bandwidth connectivity such as 400G NICs and PCIe 5.0 to support the data collection and processing required for managing increasingly complex baseboards.

Some BMCs implement advanced predictive maintenance via small AI models, to help prevent damage and wear on components, and incorporate specialised units such as NPUs to offload these small AI workloads. It's also likely that BMCs will eventually integrate more and higher bandwidth memory such as HBM stacks to cache sensor data, enabling better management functionality on chip rather than sending data to remote management servers. This shift mirrors industry's push toward "lights-out" datacentres, where fewer and fewer hardware faults require human intervention.