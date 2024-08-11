/**
 *Submitted for verification at Etherscan.io on 2020-10-01
*/

// SPDX-License-Identifier: MIT
// from file output/uni_eth_usdt.json
pragma solidity ^0.6.7;

interface ERC20 {
    function transfer(address _to, uint256 _value) external returns (bool success);
}

contract pUniEthUsdtReimbursement {
  mapping (address => uint256) public amounts;
  mapping (address => bool) public reimbursed;

  address public constant token = 0x09FC573c502037B149ba87782ACC81cF093EC6ef;
  address public constant gov = 0x9d074E37d408542FD38be78848e8814AFB38db17;

  constructor() public {
    amounts[0x907D9B32654B8D43e8737E0291Ad9bfcce01DAD6] = 3031012566706;
    amounts[0x940dBD89E5E2fA0f0A4EBFddea8E5aAa37D6C96A] = 31244835122089;
    amounts[0x01B590B256dCb6300fe43FA2c629Dd9fD2838eD4] = 63552085023437;
    amounts[0xcE156D5d62a8F82326dA8d808D0f3F76360036D0] = 33217174515224;
    amounts[0xF1394140fe0982E40fa9A9846E7c5b0842CECe56] = 417806976326662;
    amounts[0x3c879c214C2364E21a91BB6Bc300D419013E8Bf0] = 50627927339796;
    amounts[0x17a0eAE4cFa8a16D4e259C3a4ACb30E06dFf6ab6] = 40261398797072;
    amounts[0x5C5aBb7047b27c70ABec5a840f3D0C4c7759Ce8F] = 244129969815071;
    amounts[0x00FFf7e689a4ED9668c9207f55c8d68BAb1CB507] = 49840822190519;
    amounts[0xa703862d21E18A391278ae472cC2A87d34e082F6] = 809774009281242;
    amounts[0x3888F5A94560D6af334c82DC5D94C134870f9E78] = 700193908756664;
    amounts[0x4FC5A19E45De02592a4D0241869f969F68255E9c] = 62466262969544;
    amounts[0x2e4ae4d3bD0Af45040b4F17e0BB7E6dC548626B1] = 1200646239911801;
    amounts[0xEB4576fE753DAB07635c0Bb6c8f0A355e1Db5d31] = 208084588484399;
    amounts[0x6075A2c53ca8Eb6f6486e00adD1BA01AED5E6609] = 589540946655568;
    amounts[0x2bc2CA2A7B3E6EdEF35223a211aC3B0b9b8d4346] = 206795094805252;
    amounts[0x5b13bB1e315744BdEa0749cde6254f0499E25a2B] = 274425637851374;
    amounts[0xD8854167F53A57abB2a05705C58733e8f1451b5b] = 3969536602149623;
    amounts[0xF9A5EaE7E0b1D51cc8411BB612bA3B9D2cb4500A] = 82884888628616;
    amounts[0x9222f3fAD317Af2Fa4Feb4176BF3cfCE798080a6] = 44006912743740;
    amounts[0xf4828566c5976D4987F645CFB936dDd5EE5af29e] = 38884099372641;
    amounts[0x48b742b9D935FDaeADE1A48CD7c5E4aeC4360b0c] = 241021063791993;
    amounts[0x835e7e74dDc84befa0A4663d3D6AB1493A2C71b8] = 64156885303290;
    amounts[0x7Fc2F133807e2cc899c655122616B02493848B0d] = 29536993443204;
    amounts[0x42d4C197036BD9984cA652303e07dD29fA6bdB37] = 157432891463209;
    amounts[0x69eF61AFc3AA356e1ac97347119d75cBdAbEF534] = 63707139960678;
    amounts[0xdcfd6D6e63F15A391D96D1b76575Ae39Ad6965D9] = 159607923894885;
    amounts[0xE3E39161d35E9A81edEc667a5387bfAE85752854] = 101952730679861;
    amounts[0x37b66Ad48c6bf20596aC215354FD5E047011d0a3] = 605421337915201;
    amounts[0xecfaAcd495d3A63eA435C6a4b9a47EFb8E63AAF6] = 3259185427199036;
    amounts[0x904aF0Ef6115c26CBAdeab44e7b439EB5e8A22CE] = 12049779286863055;
    amounts[0xeBc462355194903ad1AD32fa767B3B74D5acA278] = 744743030089551;
    amounts[0x62f35D3231e6d3C6DDd14851Cc897b30B0c9F2Df] = 1603751236348585;
    amounts[0x26868E8eA52274617F7729c40882a4DC423b0C2e] = 2546532164569493;
    amounts[0xB288093Cb4F53d6F9B2A76750179CCBfaFcBBE38] = 680845726244386;
    amounts[0xd6809bF5D92F0A22A688208E77Ca67884d98d015] = 11917893753552;
    amounts[0x8bfad1E073b7DAE77DEC8768eA7dB33b1411455D] = 213457602470463;
    amounts[0xdDA936D9B15473489503D4B5668E7AF8ba8993B8] = 34531093414496;
    amounts[0x6977e753e022F65eBEb170d8267b2EA54a431523] = 967597409813366;
    amounts[0x48B72465FeD54964a9a0bb2FB95DBc89571604eC] = 2709102141883468;
    amounts[0xBCBE473DD45a36a97Ee612Ccf5b8b8bEA77153DA] = 79497899095722;
    amounts[0xA51A6F181D7BdE6F4fc445Ff844fa9329616C01a] = 35657439543318;
    amounts[0x0d30ca8Dc55d1b5EF9Cba4fA504dA8341e252CeC] = 607434987787402;
    amounts[0xab6bbe1FC9b0Ca95BF66f0B71DF12A0B0Ab08Be8] = 256447249764158;
    amounts[0xfb0Cc36F27a28cc19C86C156091E2BEe7B2F6b69] = 155941724914589;
    amounts[0x84aBD78727950Aa776f7939102f51Df6B166ab84] = 20938391414346;
    amounts[0xB0E1088863f02b7eDF67324d02D5093De9B19e0C] = 2847872056185140;
    amounts[0x6f6456e4Ed4f997896CA7C8D53d945D654ba45F9] = 17751442395114567;
    amounts[0xC90E339D6699a4Db5F6ffA0D21E66552b3d61d84] = 2930891725013;
    amounts[0x3B17FDd632EC7E099805B7CF049614BF9213504a] = 1578333184983049;
    amounts[0x8D4F54913BA39263395B0067F953355813223699] = 49345031145053;
    amounts[0x5F40b4E234Ce4771f70ABe5cb0a2c5253d7BD9D6] = 3024222662132229;
    amounts[0xd4f8a1BbEe54C1533CF0ef8C6f877ADa4dADcA1B] = 711818184335184;
    amounts[0x1655FbfcFEdC9d455088ff1226B6Cbe439D71DF8] = 394398411412017;
    amounts[0xb0FB18334e54A4CE487b6fb1530E1678fE8bc671] = 1198085920307621;
    amounts[0xD93e067Bcb3734F9D815F0E75E6c60B9F5539955] = 762967679602104;
    amounts[0x5802aAf121fb77530d8190cbcbda4ac8451C47aa] = 32363166793778;
    amounts[0x420E7b56927EDfd45B126a0373C4b66ce96F68C6] = 215338335648744;
    amounts[0x0B09BdeBDbd4DA9b99df5c906bEAd676b3D8F507] = 5442335359129823;
    amounts[0x87C0c0A2d4B9e39A1b6b525A2832a3e080ed6640] = 15762002969413;
    amounts[0xEBb61c0Dd09F1fF55c53bb2fF4967B2f0e4F5552] = 3574040353511231;
    amounts[0xF46AC5D16e5392d6539f1e7A2188b280197db7c7] = 31840876294895;
    amounts[0x29AaB297a1cAA0BD91DB246CEF439d1Ef92E96Bc] = 204489838716479;
    amounts[0x9cB22312B225A8a959600dC17441E0B1Bb7572a8] = 188730088493364;
    amounts[0x63950CfD75e2290a3581B6b0E39C86bC11697D5B] = 4843873029316952;
    amounts[0x66721B617dFdbcA40dBc1a92Fb0907AbB764235A] = 107632212330540692;
    amounts[0x1FcEC0f5B245Afa2B0ca81A785073d6F9DE790bb] = 15417190407343295;
    amounts[0xeaE98E98CeA0577Cf78e2Efce00B3Faa9444130C] = 616992633847359;
    amounts[0x1F47101647239C00aF2CE908521451b6a87987aA] = 248681416077387;
    amounts[0xC180cCF8D26f368563c0DD5726198822F23D6403] = 209145832874143;
    amounts[0x77fB0deBA36c1ae0057B8A07174Ed3C87F53F11E] = 674969288604915;
    amounts[0xCAB5f6B9004F1cc65eAEf965cCca998A598Cc968] = 33916522260676;
    amounts[0x11c3946dc1b186C2E8cdEbbAe4527B418a2395eE] = 4730040770271643;
    amounts[0xb6Bd92904B74dF603ffD43758755B8b0638884a1] = 15692951632312;
    amounts[0xE04FF7F17305Db881D30bcf109C3db0103C5C8b3] = 167490202482151;
    amounts[0x277CE7CE319e8aA7DB17d5784F5b24D36579Bbf7] = 22164320152153;
    amounts[0x334FF7580eE92bb13D744cd309925560877122a1] = 243033138776772;
    amounts[0x5E38b802525de11A54506801B296D2Aa93d033EF] = 155629078866638;
    amounts[0xc82c88AC3C78B8776061F34967A785eAf2003a9A] = 62122363322690;
    amounts[0xAE653682Dee958914A82C9628de794dCbbEe3D04] = 14304929069862845;
    amounts[0xDB19D3186Ea32001F6F16867D5D31a39BbA139Be] = 321605976403987;
    amounts[0x28a416E90A763B2261DC80E02a21cb7f9770B053] = 48307683932817;
    amounts[0xF96Af53BfFc1fF30d26fF3F64bA6321541F647F0] = 3394323147911;
    amounts[0x29Aec2E84d9F5AA21d423DdB80e400CAE1A49d48] = 19006459200564;
    amounts[0x11d0Cb5C690bC838eFc52C621F6B48040dd000F7] = 1188427093918296;
    amounts[0xC892b9C6192F024f9436654a13307bcF82c2fe5c] = 127104687625187;
    amounts[0xE63b7FF4639b990bAD1d7257Fff8070F859f0997] = 31730552246288;
    amounts[0x432DcBdA06e8B296CA29705572D7cb6315Ed8Bed] = 136826099282234;
    amounts[0xf6805A612FEA211f2d2785593E04830D5a1D9f29] = 170381290158958;
    amounts[0x848887741B3e38233Cd858c5dD7B48Ca9197FC08] = 20921778101860;
    amounts[0x4f862899C42645bEc4b73aB20E4d06688F592f6f] = 815487776517390;
    amounts[0x518e5A942Ed7Db4B45e9A491ce318373346dB240] = 43457959673329;
    amounts[0x9697AaBBE23C77c0df03670573e4C38253E0d49a] = 1755103665439278;
    amounts[0x0370049Eba9c196D14CA2886Dd329a700D545c72] = 696562581745922;
    amounts[0x636cF0C563B91E134e3D0c227B70CfDCDBE607F9] = 1062229168457287;
    amounts[0x8D622746dA805a5c75d32B3413C28062636e3dE9] = 940860783310663;
    amounts[0x5fd9b0B7e15B4d106624ea9CF96602996c9c344D] = 3113956987387676;
    amounts[0xDD6Fc573CF73701aa31834644E245d9fb5BF906d] = 4383010747634191;
    amounts[0x05547D4e1A2191B91510Ea7fA8555a2788C70030] = 6974601798025967;
    amounts[0x8DE0EA136082c0dDD973c6E5BF45e31f6D158973] = 2604166587169824;
    amounts[0x41C334F1a2e9Af08638947508970D7DE6189B927] = 2359893716886644;
    amounts[0x93C027865354e96a1e9ec69fc8253e6d49013f82] = 1873695157257266;
    amounts[0x120B24EC2C1fB0deE101576BE57E130E83266c8C] = 207402117177990;
    amounts[0x1Ce4C7977bf92cCf62B1DF6E97A55BC33E5E6B2F] = 207399611022335;
    amounts[0xB039dF879F41487396C6ef973272ED4db4c88c90] = 438539119288660;
    amounts[0x31E3734F5532689ADB5C1019036980A94A29BA56] = 649814398244830;
    amounts[0xa07f2A3A8a6e7F9e14CC0EB5633E6795814d549f] = 15649122817001;
    amounts[0x1c012b03f1c2DEa274D2eeEb566B0Eeabfe3Af1A] = 598524843659747;
    amounts[0x3a607Cf105e830c023003056514b86E9De0A691e] = 171868290542628;
    amounts[0xAdbfb465BCdA23F47dfAEC10AFa43C4BfC22112E] = 252982038775118;
    amounts[0xd2a81FFdF63e3a9eb47b601fdC8Bb3f23EAcD795] = 286924503558618;
    amounts[0x51f9946A9e4a8c8F64F335942609ed2bd9C027ad] = 7144696155386;
    amounts[0xd3A349dC7CBfafBEe996528Ad3C3839940786486] = 2073901065568;
    amounts[0x51Ca31fc7eFB55db794378695eF3506AbA0883D2] = 655584575068538988;
    amounts[0x79e14e09e99348DbDa367a594EDDCA08a7FCe728] = 2994742440140199;
    amounts[0x132B7b7cc37b399a813e26DB4e8D219c377f0EC7] = 1856936733447491;
    amounts[0xdf8d12A07540768032aa307D50aF6CB5F4e8c153] = 5550162801725746;
    amounts[0xd74A1d8375eEdC1e79Aa8B811d197746C1B559C6] = 5906539331213;
    amounts[0xa2888a8B86fbc2BCe538305257003E7159a9192F] = 729269701927193;
    amounts[0x36bBD1EF1Fd15637d63dE4ccB4EfA49EA1F053e8] = 340332718914844;
    amounts[0x108156f882a065148e1De97F877195d6C4942B94] = 103824875262002;
    amounts[0x13bbb69C3C2E4358A1c012E057D5Fe4B56E55513] = 50730639905003;
    amounts[0x331c37F833b6929199704c0c49Cdf4903DE13799] = 884871907559915;
    amounts[0x310D5C8EE1512D5092ee4377061aE82E48973689] = 1855104189659456;
    amounts[0x0D4F36CAE5998C47428849A5727E2A041B7a411C] = 51958167243340918;
    amounts[0x044a9c43e95AA9FD28EEa25131A62b602D304F1f] = 497135758298119;
    amounts[0x800C49b4A5bAC2aC16f045037F8fbAC255b62eC9] = 405117967245221;
    amounts[0x1092361f4eAfDC6e4555Ee761E87Ef9c67b9e42f] = 36757227583537;
    amounts[0xc3721AeC7BACb81e8b4a26935959Ad712e1dE2A5] = 37993697523976;
    amounts[0x6bac48867BC94Ff20B4C62b21d484a44D04d342C] = 12557759352144;
    amounts[0x8B851F5C530e99ed988887CD58eF0338f8E09B7A] = 22616852856828;
    amounts[0x47FEA52a4b79954fEdE50EE07b3F5d22696c8586] = 99934549569912;
    amounts[0x304BFB9BDd5fae5c93beE3dB6Fb7407717Ff3106] = 10580365463517475;
    amounts[0xAA421C0ECE2ca7d7d834900BC898B872036FD792] = 236640492215019;
    amounts[0x76Da9F88e63a85Ba8BFA19F3821D5A271753D3dc] = 6823581133399;
    amounts[0x5b1253A732d9c2B90CA0815631202A912589ABc8] = 13389722558653;
    amounts[0xAcDB30e0Faa07f274687aCeAA41Ecf3dC2a26747] = 433164124180439;
    amounts[0x802dAC771D2C71afB5F323B1fAd4E4320EeA2Dc7] = 3405051177070611;
    amounts[0x1bB7BA2e4104d68448567e75912C329fe9fA9204] = 1003125405745109;
    amounts[0x4996De5A4e624fCE5A718B2a2547901fB050C2B4] = 1389434957857971;
    amounts[0xcd4131D881F8a6797993c15B3FF1BD8505f76788] = 2110115890408967;
    amounts[0xf7932e4CaAb9d96be9ac85505E7a13DD3625aA19] = 1044997648591776;
    amounts[0x44f51503b633060BBD54963710dA9888A8BA5b49] = 54555924508578847;
    amounts[0xD781f6729d033542c5377cE9ec68eD4b44f07378] = 245889954631654;
    amounts[0xc0819E1e01204BCB9CB5a0a3Be826afedAd6EDEf] = 14717040520476416;
    amounts[0x82d09D4032e0c71379f314B49ecaf68Cf4FACF36] = 2309154015248;
    amounts[0x5c4D8CEE7dE74E31cE69E76276d862180545c307] = 38031757081821;
    amounts[0x164a15E16D697c2F8aC77c2866441f411365D396] = 31278666190304;
    amounts[0x7bA6372DfEe7eae56C9fA96Cd477455E8a4B2C6D] = 51973110491362684;
    amounts[0x1CBd88790b7324DfFC5F4549e2286000bCa1156A] = 2674063728182211;
    amounts[0xA94ca3837fa92D3223f0b651C5672299F286158d] = 12919675663368636;
    amounts[0xd86D40cCbc02ea258c442185BF16F16D6336Fc1B] = 28312442729760630;
    amounts[0x36bed53B24f982ea2f4b231b3763Cf453401E50D] = 3258190910273;
    amounts[0x3735773a5Aa173c2d576A27185B233CA4c5510b5] = 1286628236366573;
    amounts[0x0C5a2C72C009252f0E7312f5a1Ab87de02be6FBE] = 216416511257781;
    amounts[0x005Ff202C271d2419fb03ec873DEdFe163A5ce36] = 211240414990327;
    amounts[0x0300FB2560DDf901B9bC408b119AcA8f0143304A] = 4645800642603808;
    amounts[0x577BE3eD9A71E1c355f519BBDF5f09Ba2018b1Cc] = 88456118382263;
    amounts[0x4Eb7F19D6eFcACE59EaED70220da5002709f9B71] = 7468169953183;
    amounts[0xB6a0794da7846c4f016880c8fd7C43FebA7E7440] = 3296666278987;
    amounts[0x25d87832BE2B87c6a99e8764e50f387e49028e92] = 21799144757439;
    amounts[0x79C4213a328E3B4F1D87b4953C14759399dB25E2] = 270257499735574;
    amounts[0x5bC6a64275391dD2D79CF0431DbDD888E5Ef35F1] = 82807506975480;
    amounts[0x007bbEc99CD6239923F4667998b8A47204EB0cD2] = 2031439415626861;
    amounts[0x44E2F285F26bF65b5396873dD25B8D82A63e5546] = 906043389573153;
    amounts[0x4347e44D5ddf158d692Ff86eA7df813AD799a990] = 249121098575197;
    amounts[0xFB3A939Cb06eeF36E1ceD48bdba1fcEe177Ac7f4] = 1841206680740;
    amounts[0xFBb05840f992396e1Aaaa34A6d25CCcE86a27559] = 15183419009183;
    amounts[0x63174da8d75218d869804469cdFb507fd612E4ff] = 942779251297296;
    amounts[0x64A302b702951C8106d4B4D3033C75D0Bed3b138] = 141911918643691;
    amounts[0x4e7CD3458CdA9c75C39C40b4393108141ba0e2f7] = 3806842323001;
    amounts[0x0cc8a5b61482253860f7C551232c0244004AF5aC] = 170482962755065;
    amounts[0x1E3882aFF34C1eaF5507e77026F215085bda1e19] = 298012238138859;
    amounts[0x9FaCE78A611e257c707665A28CeEe658e93e2a59] = 647032432851903;
    amounts[0x64AD5E331BDEb2F6dE21Ca1FCC17604cF724130C] = 284776189310900;
    amounts[0xb92667E34cB6753449ADF464f18ce1833Caf26e0] = 61702402528859;
    amounts[0xF219809386C7ad810FaeB9765FBFc7642A625196] = 1515284800851;
    amounts[0x88ee5532815DDd0cd009A556F44b42322083f193] = 2344515053785550;
    amounts[0x198ac692a69953D7Cfd6b484801B8400aF16F8d4] = 5643067175243;
    amounts[0x7682161c9fbe3A4065B38c2CD3ca61263Fe27769] = 15223576661210;
    amounts[0xC8C8Ea2588D9E26A69c2fa56C09C7e274b72D8A0] = 92813664865893;
    amounts[0x20f9ddFA193D0fe2f73d8b7D749B1355eF019887] = 4561736681154408;
    amounts[0x928477dabc0eD2a6CE6c33966a52eA58CbDEA212] = 1518714052822689;
    amounts[0x099be8A016843839Ab52F369678541b2Ac8bfCA1] = 1041226594002623;
    amounts[0xE9DEe6Fbb67BC2E71e322e15AE7c6076223d566e] = 941484459342075;
    amounts[0xf1246624EBDACAE1e3A576949e39321D0201ecB9] = 2231029061907;
    amounts[0xf2e66768A8469A48E2eF282b006cD886147b4CB0] = 158980796192189;
    amounts[0xC6eB98c4A9657b9A11F725cB6BaC22fDE93a7F3a] = 1280605295121410;
    amounts[0x069e86e2F5F64D482c917ab18F7b48A2Dae4Cc3d] = 224447068994848;
    amounts[0xc9D3709156A253d83eBf482A059817097fE6856A] = 814981072819514;
    amounts[0x698fa6437475F3F86Df33eA0cb612AD529954811] = 1286814337966;
    amounts[0xbEc6E4AC010114e515483060FDA81Cf9088040fF] = 2381130366085491;
    amounts[0x7a2611B4b14D14c6d57C39daC5B02cb15Ef5Eef6] = 4709166288738;
    amounts[0x400cBCF4B2A30AAC711Fc5A882FcAF485ccE6F04] = 15185910080574;
    amounts[0x4b8515d6Aa44eAA0d0587D395CF52f26dD25F91E] = 428665977970;
    amounts[0x058B10CbE1872ad139b00326686EE8CCef274C58] = 1;
    amounts[0xbdAD8d6ea11b590DC0a5ae002227CDBDF1c4DDD6] = 850983243;

  }
  
  function claim() public {
    require(!reimbursed[msg.sender], "already reimbursed");
    require(amounts[msg.sender] > 0, "not claimable");
    require(ERC20(token).transfer(msg.sender, amounts[msg.sender]));
    reimbursed[msg.sender] = true;
  }

  function saveERC20(address _erc20, uint256 _amount) public {
    require(_erc20 != token, "!token");
    require(ERC20(_erc20).transfer(gov, _amount));
  }
  
}