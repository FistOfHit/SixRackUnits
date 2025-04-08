[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# January 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/1.png)

*A person comparing their own size to the earth would have an easier time comprehending that size difference than trying to compare the size of a transistor to the chip it has been etched into.*

[**This month's updates:**](#this-months-updates)
  - [**DeepSeek possibly under-reports AI hardware infrastructure**](#deepseek-possibly-under-reports-ai-hardware-infrastructure)
  - [**Samsung and Micron still in the race for HBM**](#samsung-and-micron-still-in-the-race-for-hbm)
  - [**Mixed market sentiment on Nvidia's GB200 rack-scale SKUs**](#mixed-market-sentiment-on-nvidias-gb200-rack-scale-skus)
  - [**Qualcomm and Arm to compete over datacentre Arm CPUs**](#qualcomm-and-arm-to-compete-over-datacentre-arm-cpus)
  - [**The incredible engineering of Nvidia's RTX 5090**](#the-incredible-engineering-of-nvidias-rtx-5090)

[**Vendor spotlight:**](#vendor-spotlight)
  - [**GigaIO**](#gigaio)

[**One-pagers:**](#one-pagers)
  - [**Overclocking**](#overclocking)
  - [**Intel's AVX/AMX – Advanced Vector/Matrix eXtensions**](#intels-avxamx-advanced-vectormatrix-extensions)

For a space to share sources and news/updates, join on <a href="https://t.me/aihpc_infra_fans">Telegram</a>, and check out my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

* * *

# This month's updates:

## DeepSeek possibly under-reports AI hardware infrastructure

_The AI model that wiped an estimated $1.5 Trillion in value off global stocks was not an automated trading or banking service gone wrong, but just a free to use - and very capable - chatbot. DeepSeek's R1 was reportedly trained on just 2048 H800 GPUs, but some sources claim that significantly more compute was used._

Though [the paper](https://arxiv.org/abs/2501.12948) claims that only 2048 Nvidia H800 GPUs and 5.6M USD were used during model training, [speculation](https://www.aljazeera.com/news/2025/1/29/ai-game-changer-or-overhyped-deepseek-faces-scrutiny-over-bold-claims) and [rumours](https://www.tbsnews.net/tech/chinas-deepseek-faces-questions-over-claims-after-rattling-us-tech-market-1055846) from industry have brought the legitimacy of this statement into doubt. DeepSeek (owned by Chinese hedge fund "High-flyer") open-sourced their free-to-use "R1" model and shocked the market by quickly reaching second place on various public leaderboards and benchmarks, just short of OpenAI's o1. What's more, the model is [significantly smaller and cheaper to run than its American/European counterparts](https://artificialanalysis.ai/models) and is freely available for anyone to build upon and run locally. But many sources claim it's likely that DeepSeek used a lot more compute than they report.

Huida (Nvidia's trading name in the Chinese market) designed the H800 AI accelerator in response to the [2022 US chips act](https://en.wikipedia.org/wiki/CHIPS_and_Science_Act), with it being essentially a reduced bandwidth H100 tailored to avoid export restrictions and meet the high demand for AI training compute from restricted countries. [Both accelerators are almost equivalent](https://www.fibermall.com/blog/nvidia-ai-chip.htm?srsltid=AfmBOoqbmALiePZjY4PjSI-_rcNmmze4QcvJLVT0PHyNHTJC4UMqctPc) except for the H800 supporting only 8 x 50GB/s NVLink channels instead of the 18 available on H100s. ScaleAI CEO Alexandr Wang states that industry rumours hint at [DeepSeek owning over 50,000 H100 GPUs](https://www.tbsnews.net/tech/chinas-deepseek-faces-questions-over-claims-after-rattling-us-tech-market-1055846), likely acquired through Singapore to circumvent trade restrictions, and [SemiAnalysis stating](https://semianalysis.com/2025/01/31/deepseek-debates/) that its more likely about 10,000 each of the H800 and H100s, with 30,000 H20s

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/2.png)

Based on their ["Fire-flyer" paper](https://arxiv.org/pdf/2408.14158), it's evident that DeepSeek staff have extensive experience in optimising and maintaining infrastructure containing thousands of Nvidia GPUs with InfiniBand fabrics. The paper outlines how they designed and benchmarked a cluster of ~10,000 A100 GPUs, significantly deviating from Nvidia reference architecture for large cost reductions with relatively small performance drops. Most notably, their use of Connecting GPUs and IB NICs to CPUs via PCIe ports directly with no switching and developing their own collective communications library "HFReduce" which outperforms NCLL on their P2P NVLink setup, are both unique and very resourceful initiatives.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/3.png)

*Source: Highflyer*

## Samsung and Micron still in the race for HBM

_Last quarter, SK-Hynix and Nvidia both confirmed plans for 6th gen. HBM4 with the memory manufacturer agreeing to meet the 1H2025 deadline for sampling their devices on Nvidia's "Rubin" architectures. Now, Samsung and Micron both formally announce that they too are still competing for the future of this market._

In mid-4Q24, [Nvidia requested SK-Hynix to accelerate their development of HBM4 devices](https://www.tomshardware.com/pc-components/gpus/nvidia-asked-sk-hynix-to-accelerate-hbm4-chip-delivery-by-six-months-says-report), preparing samples for testing and validation on Nvidia's "Rubin" prototypes due in 2Q25. This resulted in them bringing forward their roadmap by 6 months, setting the date for mass production to the end of 3Q25, a [timeline that originally had not been shared by their competitors](https://www.trendforce.com/news/2025/01/13/news-samsung-reportedly-speeds-up-hbm4-by-6-months-as-nvidia-plans-early-rubin-launch-in-q3/#:~:text=Originally%2C%20Samsung%20planned%20to%20begin%20mass%20production%20of%20HBM3E%20in%20the%20first%20half%20of%202025.%20However%2C%20it%20now%20seems%20that%20speeding%20up%20the%20development%20of%20HBM4%20has%20become%20the%20top%20priority%20for%20memory%20giants.).

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/4.png)

Now, to regain their shrinking share of the HBM market, Samsung announced that [they too will be releasing HBM4 samples for the end of 2Q25](https://www.trendforce.com/news/2025/01/06/news-samsung-reportedly-starts-trial-production-of-hbm4-logic-die-with-in-house-4nm-node-challenging-sk-hynix/), likely to compete for the same trials on Nvidia hardware. It's unclear whether Samsung will meet this deadline due to recent heat/power management issues with their (4th and 5th gen.) implementations, with [Nvidia repeatedly failing Samsung's attempts at passing validation](https://www.datacenterdynamics.com/en/news/samsung-hbm3-chips-finally-pass-nvidia-tests-but-wont-be-used-in-top-gpus-report/). Their specific HBM4 designs also reportedly include using [world-leading 1c 10nm DRAM dies, with logic dies being incorporated into the device](https://www.mk.co.kr/en/business/11165432) for multiple, smarter buffers and providing some compute-in-memory capabilities. On top of this, [Samsung also have declared intent to develop custom HBM4 devices](https://www.mk.co.kr/en/business/11165432) for chip manufacturers such as Microsoft and Meta who are likely to be in the market for memory with narrower bus widths and higher overall density.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/5.png)

In addition, Micron, the smallest of the 3 major memory manufacturers has announced that they are [conducting final tests for their implementation of high-density 16hi HBM3e](https://www.trendforce.com/news/2025/01/15/news-micron-races-to-catch-up-with-sk-hynix-reportedly-conducts-final-tests-for-16h-hbm3e-production/), with mass production due before 2026. Despite being behind SK-Hynix in 16hi, Micron might well have a better chance than Samsung of increasing their HBM market share over the next year due to [them famously winning the Nvidia H200 contract for 8hi HBM3e](https://investors.micron.com/news-releases/news-release-details/micron-commences-volume-production-industry-leading-hbm3e) and hence being able to make significant investments in expanding their production capacity over the coming years. Unlike the other two, Micron keeps its [HBM4 mass production plans to 2026/27](https://www.techradar.com/pro/micron-wants-a-bigger-slice-of-the-usd100-billion-hbm-market-with-its-2026-bound-hbm4-and-hbm4e-memory-solutions).

## Mixed market sentiment on Nvidia's GB200 rack-scale SKUs

_Nvidia's B200 GPUs might possibly be at the centre of another overheating issue, this time stemming from the extreme density of their rack-scale SKUs, the NVL36/72s. Taiwanese suppliers such as Foxconn, Winstron, and QCT amongst the largest, claim that these rumours are incorrect and that orders are being fulfilled as expected._

[From as far back as mid-3Q24](https://www.networkworld.com/article/3608212/nvidia-blackwell-chips-face-serious-heating-issues.html), rumours have been circulating of Nvidia's "Blackwell" rack SKUs experiencing overheating issues, causing issues for major customers such as Microsoft and Amazon. Recently, [these reports have resurfaced](https://www.trendforce.com/news/2025/01/14/news-nvidia-gb200-racks-reportedly-overheat-major-clients-cut-orders/) as reductions in order volumes and an increase in demand for older "Hopper" H1/200 GPUs have been confirmed, with [OpenAI reportedly asking Microsoft to provide more capacity on H100s](https://www.reuters.com/technology/artificial-intelligence/nvidias-biggest-customers-delaying-orders-latest-ai-racks-information-reports-2025-01-13/) to make up for the delays.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/6.png)

*Source: Nvidia*

With B200s having a TDP of up to 1000W and Grace CPUs designed for 500W, a single 1RU GB200 tray with 2 Grace and 4 Blackwell chips is [estimated to have a maximum power draw of ~6300W](https://semianalysis.com/2024/07/17/gb200-hardware-architecture-and-component/) under sustained high utilisation, requiring advanced direct liquid cooling solutions that [very few datacentres in the world have the infrastructure for](https://www.jll.co.uk/en/trends-and-insights/workplace/liquid-cooling-enters-the-mainstream-in-data-centers#:~:text=%E2%80%9CA%20liquid%20cooling%20installation%20eliminates,to%20be%20converted%20into%20additional). In total, an NVL72 rack holds 18 such compute trays as well as 9x1RU NVswitch trays for the GPU-GPU data fabric, all connected with active copper cabling. Whilst [a variety of OEMs](https://www.hpcwire.com/2024/11/18/hpe-and-dell-lay-the-groundwork-for-next-gen-supercomputers/) have now released their own implementations of the liquid cooled GB200 NVL72, it's likely that testing outside of curated lab environments has been rare.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/7.png)

*Source: Nvidia*

Taiwanese manufacturers and integrators such as [Foxconn, Winstron, and QCT all deny these rumours](https://www.tweaktown.com/news/102606/taiwan-suppliers-for-nvidia-gb200-ai-servers-components-rumors-of-overheating-are-wrong/index.html), reporting that the current shipments are on schedule and are not affected by overheating issues. Instead, analysts cite [cost vs benefit calculations compared to the tried and tested H1/200 HGX servers](https://wccftech.com/taiwanese-server-manufacturers-deny-overheating-issues-with-nvidia-gb200-ai-servers/) that are widely available to many buyers, as well as the [timeline for Nvidia's B300 (previously named the B200 Ultra) and "Rubin" series GPUs](https://www.reuters.com/technology/artificial-intelligence/nvidias-biggest-customers-delaying-orders-latest-ai-racks-information-reports-2025-01-13/) being close enough to affect ordering times for hyperscalers.

## Qualcomm and Arm to compete over datacentre Arm CPUs

_Another established mobile chipmaker now moving into the datacentre CPU space, Qualcomm has been hiring for server design roles recently. At the same time Arm may be preparing for an acquisition of the high-performing Arm CPU designer, Ampere._

With Nvidia's Grace chips having [shown success in the Arm server CPU market](https://www.nextplatform.com/2024/02/06/nvidias-grace-arm-cpu-holds-its-own-against-x86-for-hpc/) - albeit likely due to them being packaged in the GB200 rack-scale SKUs - and [Apple showing signs of entering the same space with names such as Broadcom and Foxconn](https://www.theregister.com/2024/12/12/apple_ai_chip_broadcom/), it was always expected that other semiconductor design teams would follow suit. Now, both Qualcomm and Arm appear to be taking significant actions towards this, with aggressive hiring and discussions of acquisitions.

Qualcomm, having previously forayed into this space in [2017 with their Centriq 2400 series](https://en.wikipedia.org/wiki/Qualcomm_Centriq), couldn't gain significant traction in the market due to the dominance of x86-based competitors and the difficulty of porting many applications to Arm architectures. Now, preferences and capabilities in industry have [shifted towards energy efficiency](https://www.grandviewresearch.com/industry-analysis/arm-based-servers-market-report), evidenced by a movement towards names such as Nvidia's grace, Ampere's Altra, and AWS's Graviton to name a few. To confirm their intent, Qualcomm have [hired Intel's server CPU lead](https://www.crn.com/news/components-peripherals/2025/qualcomm-hires-intel-xeon-server-cpu-chief-architect#:~:text=Qualcomm%20Hires%20Intel%20Xeon%20Chief%20Architect%20Amid%20Server%20CPU%20Plans,-By%20Dylan%20Martin&text=Sailesh%20Kottapalli%2C%20a%2028%2Dyear,the%20data%20center%20CPU%20market.) and have been openly looking for [other CPU and server design roles.](https://www.datacenterdynamics.com/en/news/qualcomm-poaches-intel-server-engineer-is-hiring-architects-to-develop-data-center-processors/)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/8.png)

At the same time, Arm have reportedly entered [discussions along with SoftBank on acquiring Ampere](https://www.reuters.com/technology/softbank-arm-weigh-acquiring-ampere-computing-bloomberg-reports-2025-01-09/), the market leader now in high performance, high core-count ARM server CPU. Until now, Arm has kept to developing and licensing semiconductor IP such as their individual cores for mobile and server applications (the [Cortex](https://en.wikipedia.org/wiki/ARM_Cortex-M) and [Neoverse](https://en.wikipedia.org/wiki/ARM_Neoverse) series) which have seen success in processors made by Nvidia, AWS and Google to name a few. Ampere, on the other hand develop very high-core count processors such as their [96-192 core "AmpereOne" M and MX](https://amperecomputing.com/briefs/ampereone-family-product-brief) series and their [upcoming "Aurora" 512-core SKU](https://www.servethehome.com/ampere-ampereone-aurora-512-core-ai-cpu-announced-arm/) scheduled for 2025. Some of the concerns that regulators might have include possible conflicts between existing licensing agreements, Oracle's 29% share in Ampere, and Ampere's own plans for an IPO which are still underway.

## The incredible engineering of Nvidia's RTX 5090

_Nvidia showcases their expertise in the gaming GPU space with their latest series of RTX graphics card built on their new "Blackwell" architecture. For the 5090 - the most performant GPU in the lineup - early samples have already been taken apart and reverse engineered, revealing just how unique its engineering is._

[At their CES keynote](https://blogs.nvidia.com/blog/ces-2025-jensen-huang/) earlier this month, Nvidia officially revealed the entire RTX 50XX series, though samples had likely been sent to various testing and review groups [as far back as December](https://www.tomshardware.com/pc-components/gpus/nvidias-unreleased-rtx-5090-pictured-with-huge-gpu-die-sports-32gb-of-gddr7-memory). Among the many reviewers, [the Der8auer group](https://youtu.be/qwOQWcg-Z_A?feature=shared) - who received a special "Founders edition" (FE) version of the 5090 – commented on how each of the 58 cooling fins are uniquely shaped, resulting in just two fans able to manage a device with a TDP of 575W in a FHFL PCIe form factor.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/9.png)

*Source: Nvidia*

Its counterpart in the current generation, [the RTX 4090 as released in 2022](https://www.nvidia.com/en-gb/geforce/graphics-cards/40-series/rtx-4090/), was notably difficult to acquire due to cryptocurrency miners and low-tier AI datacentres using it as a cheaper and more efficient option than datacentre grade devices which are priced for the enterprise and require warranties and licensing among other things. The RTX 5090 reference design (RD) which will be sold as the standard version is similarly [expected to be extremely difficult to buy](https://wccftech.com/nvidia-geforce-rtx-50-series-gpus-facing-shortages-ahead-of-launch-rtx-5090-5080-price-surge/) due to incredible demand.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/10.png)

*Source: Nvidia*

As for its specs ([1](https://en.overclocking.com/der8auer-reviews-the-nvidia-rtx-5090-fe/) [2](https://www.eurogamer.net/digitalfoundry-2025-nvidia-geforce-rtx-5090-review) [3](https://www.theverge.com/2025/1/23/24349619/nvidia-rtx-5090-review-test-benchmark) [4](https://www.techradar.com/computing/gpu/nvidia-geforce-rtx-5090)):

* Using TSMCs 4nm process node
* 92.2B transistors in total within 744mm2
* 21,760 CUDA cores
* Clocking up to 2.4GHz (2.54 for the FE)
* 32GB of GDDR7 (512-bit bus width)
* 1.79TB/s memory bandwidth
* Air-cooled TDP of 575W
* PCIe 5.0 x16 in a FHFL form factor
* 680 5th gen. Tensor cores
* Starting at ~$2000 (estimated)

* * *

# Vendor spotlight:

## GigaIO

_A relatively small American OEM, [GigaIO](https://gigaio.com/) decided to forgo integrating network fabrics tightly with compute and memory and instead decided to extend PCIe to outside the chassis. With their incredibly underrated "FabreX" tech stack, they're able to connect up to 64 nodes and present them as one "giga node" to software._

Optimised for edge inferencing, the Gryf suitcase-sized supercomputer packs up to 2.5KW in a airplane form factor. Gryf comes with six field-replaceable sleds that can be customised between four categories - compute, AI accelerator, networking, and storage units. The sleds are all internally connected by a FabreX backend network as well as allowing for up to 100GbE scale out, and multiple Gryf units can be connected using FabreX as a scale-up fabric. Currently, the compute sleds support 64 core AMD Milan CPUs, and the AI accelerators that fit the size and power envelope are limited to Nvidia's L40S, though it appears other FHFL options are being qualified currently. Storage sleds have a capacity of up to 246TB, leading to well over a PB of managed storage in a Gryf optimised to act as a GPFS server.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/11.png)

*Source: GigaIO*

The FabreX networking stack essentially takes PCIe out from within the confines of a chassis and allows for composing a large amount of compute resources over many physical servers into one giant virtual machine. Technology like this does already exist but suffers from a variety of limitations and performance issues due to the challenges involved in virtualising away many different communication protocols and networking stacks. With FabreX, everything is within the PCIe domain, and so using GigaIO's FabreX NICs and switches, everything can appear as if it is on one motherboard. This allows for aggregating large amounts of compute resources such as up to 64 GPUs into one virtual server, or for dynamically changing the setup of a machine to vary the amount of memory or networking available. This has led to a variety of bold claims that GigaIO makes on the performance of their solutions.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/12.png)

*Source: GigaIO*

* * *

# One-pagers:

## Overclocking

_When power draw and cooling are no longer concerns, overclocking can offer a way to get more performance from the same hardware quickly, though the types of applications that can benefit from pushing CPUs and GPUs beyond their recommended bounds are limited._

All digital processors execute tasks by breaking them into "cycles", synchronized to an internal clock - a high-frequency signal measured in mega/gigahertz (M/GHz). Each cycle allows the processor to perform operations like fetching data, executing instructions, or writing results. Modern CPUs use techniques such as pipelining to overlap these tasks across multiple cycles, but all operations are still tied to the clock's rhythm. For example, a CPU might complete 1–4 instructions per cycle depending on its architecture. The clock rate - essentially the speed of this internal metronome - directly influences how quickly these operations occur. Higher clock speeds reduce latency for tasks like gaming or single-threaded applications, where rapid execution of individual instructions matters most.

However, increasing the clock rate (overclocking) comes with trade-offs. While it boosts performance, it also raises power consumption and heat output, with each 10% increase in clock speed typically raises power draw by 20-30%, straining cooling systems and risking thermal throttling.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/13.png)

*Source: Intel*

Modern CPUs use dynamic frequency scaling to balance efficiency and performance, but overclocking bypasses these safeguards, prioritizing raw speed. This involves manually adjusting the CPU's clock rate and voltage via BIOS settings or software tools, often used by gamers and enthusiasts to maximize frame rates or benchmark scores. Some AI workloads, like small-scale inference, may also benefit from faster serial computations, though parallel tasks (e.g., large-scale model training) depend more on core count and memory bandwidth.

CPUs typically offer a wide variation in allowable clock rates due to the inherent flexibility of their design and having to orchestrate the various components of a server such as memory and I/O, whereas GPUs and more application-specific processors tend to have a narrower acceptable range.

## Intel's AVX/AMX – Advanced Vector/Matrix eXtensions

_Application performance on any processors depends not only on the inherent capability of the hardware, but also the software that runs on top of it. Intel's AVX/AMX (advanced vector/matrix extensions) are instruction sets add-ons that optimise the use of Intel CPU/NPUs for modern data-heavy workloads._

Modern CPUs rely on instruction sets - collections of commands that define how hardware processes data - to execute tasks. AVX, introduced in 2011, expanded Intel's x86 capabilities by adding 256-bit vector registers (YMM), enabling CPUs to perform operations on multiple data points, from 4 x FP64 to 32 x Int8 simultaneously. AVX accelerated tasks like image processing, physics simulations, and machine learning inference, where identical operations on large datasets benefit from parallel execution. Later, AVX-512 (2016) doubled register width to 512 bits (ZMM), further boosting throughput for scientific computing and AI training, though at higher power costs. However, with AI workloads demanding even higher arithmetic intensity, a newer instruction set with additional data structures was needed.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/january_2025/images/14.png)

AMX, launched in 2023 with Intel's Sapphire Rapids CPUs, targets matrix operations by introducing 2D tiles, which are dedicated on-chip memory blocks for matrix operations. Unlike AVX's general-purpose registers, AMX tiles are optimized for matrix multiplications, a core operation in neural networks. Using tiles allow developers to further optimise processing very large regions of memory by exploiting locality and parallelism further. This design mirrors GPU-style efficiency for AI tasks while retaining CPU flexibility for mixed workloads. For example, a CPU with AMX can handle both database queries and real-time inference to a degree, making it ideal for edge AI or hybrid cloud environments.

AVX and AMX reflect Intel's strategy to bridge the gap between CPUs and specialized accelerators. AVX's vector parallelism suits diverse workloads, from video encoding to physics simulations, while AMX's matrix focus competes directly with GPUs in AI efficiency. Though AVX-512's power demands limit its adoption, AMX's lower energy footprint positions it as a scalable AI solution suitable for high-bandwidth CPUs such as Sapphire rapids onwards.

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)